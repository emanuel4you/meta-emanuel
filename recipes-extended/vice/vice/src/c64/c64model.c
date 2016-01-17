/*
 * c64model.c - C64 model detection and setting.
 *
 * Written by
 *  Hannu Nuotio <hannu.nuotio@tut.fi>
 *  groepaz <groepaz@gmx.net>
 *
 * This file is part of VICE, the Versatile Commodore Emulator.
 * See README for copyright notice.
 *
 *  This program is free software; you can redistribute it and/or modify
 *  it under the terms of the GNU General Public License as published by
 *  the Free Software Foundation; either version 2 of the License, or
 *  (at your option) any later version.
 *
 *  This program is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *  GNU General Public License for more details.
 *
 *  You should have received a copy of the GNU General Public License
 *  along with this program; if not, write to the Free Software
 *  Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA
 *  02111-1307  USA.
 *
 */

#include "vice.h"

#include <string.h>

#include "c64-resources.h"
#include "c64model.h"
#include "cia.h"
#include "machine.h"
#include "resources.h"
#include "sid.h"
#include "types.h"
#include "vicii.h"

/******************************************************************************/

#define CIA_MODEL_DEFAULT_OLD CIA_MODEL_6526
#define CIA_MODEL_DEFAULT_NEW CIA_MODEL_6526A

static int c64model_get_temp(int vicii_model, int sid_model, int glue_logic,
                             int cia1_model, int cia2_model, int new_luma, int board, int iecreset,
                             const char *kernal, const char *chargen);
static void c64model_set_temp(int model, int *vicii_model, int *sid_model,
                              int *glue_logic, int *cia1_model, int *cia2_model,
                              int *new_luma, int *board, int *iecreset,
                              const char *kernal, const char *chargen);

/******************************************************************************/

static int is_new_sid(int model)
{
    switch (model) {
        case SID_MODEL_6581:
        case SID_MODEL_6581R4:
        default:
            return 0;

        case SID_MODEL_8580:
        case SID_MODEL_8580D:
            return 1;
    }
}
static int is_new_cia(int model)
{
    switch (model) {
        case CIA_MODEL_6526:
        default:
            return 0;

        case CIA_MODEL_6526A:
            return 1;
    }
}

struct model_s {
    int video;   /* machine video timing */
    int luma;    /* old or new */
    int cia;     /* old or new */
    int sid;     /* old or new */
    int board;
    int iecreset;
    char *kernalname;
    char *chargenname;
};

static struct model_s c64models[] = {
    { MACHINE_SYNC_PAL,     1, 0, 0, 0, 1, "kernal", "chargen" },
    { MACHINE_SYNC_PAL,     1, 1, 1, 0, 0, "kernal", "chargen" },
    { MACHINE_SYNC_PAL,     0, 0, 0, 0, 1, "kernal", "chargen" },
    { MACHINE_SYNC_NTSC,    1, 0, 0, 0, 1, "kernal", "chargen" },
    { MACHINE_SYNC_NTSC,    1, 1, 1, 0, 0, "kernal", "chargen" },
    { MACHINE_SYNC_NTSCOLD, 0, 0, 0, 0, 1, "kernal", "chargen" },
    { MACHINE_SYNC_PALN,    1, 0, 0, 0, 1, "kernal", "chargen" },
    /* SX64 FIXME: guessed */
    { MACHINE_SYNC_PAL,     1, 0, 0, 0, 1, "sxkernal", "chargen" },
    { MACHINE_SYNC_NTSC,    1, 0, 0, 0, 1, "sxkernal", "chargen" },
    /* C64 Japanese FIXME: guessed */
    { MACHINE_SYNC_NTSC,    1, 0, 0, 0, 1, "jpkernal", "jpchrgen" },
    /* C64 GS FIXME: guessed */
    { MACHINE_SYNC_PAL,     1, 1, 1, 0, 0, "gskernal", "chargen" },
    /* PET64 FIXME: guessed */
    { MACHINE_SYNC_PAL,     1, 0, 0, 0, 1, "edkernal", "chargen" },
    { MACHINE_SYNC_NTSC,    1, 0, 0, 0, 1, "edkernal", "chargen" },
    /* ultimax FIXME: guessed */
    { MACHINE_SYNC_NTSC,    1, 0, 0, 1, 1, "kernal", "chargen" },
};

/* ------------------------------------------------------------------------- */
static int c64model_get_temp(int video, int sid_model, int glue_logic,
                      int cia1_model, int cia2_model, int new_luma, int board, int iecreset,
                      const char *kernal, const char *chargen)
{
    int new_sid;
    int new_cia;
    int i;

    if (cia1_model != cia2_model) {
        return C64MODEL_UNKNOWN;
    }

    new_sid = is_new_sid(sid_model);
    new_cia = is_new_cia(cia1_model);

    for (i = 0; i < C64MODEL_NUM; ++i) {
        if ((c64models[i].video == video)
            && (c64models[i].luma == new_luma)
            && (c64models[i].cia == new_cia)
            && (c64models[i].sid == new_sid)
            && (c64models[i].board == board)
            && (c64models[i].iecreset == iecreset)
            && (kernal ? !strcmp(c64models[i].kernalname, kernal) : 1)
            && (chargen ? !strcmp(c64models[i].chargenname, chargen) : 1)) {
            return i;
        }
    }

    return C64MODEL_UNKNOWN;
}

/* get model from details */
int c64model_get_model(c64model_details_t *details)
{
    return c64model_get_temp(details->vicii_model, details->sid_model, details->glue_logic,
                             details->cia1_model, details->cia2_model, details->new_luma, 
                             details->board, details->iecreset, details->kernal, details->chargen);
}

int c64model_get(void)
{
    int video, sid_model, cia1_model, cia2_model, new_luma, board, iecreset;
    char c[0x10], k[0x10];
    const char *chargen = c, *kernal = k;

    if ((resources_get_int("MachineVideoStandard", &video) < 0)
        || (resources_get_int("SidModel", &sid_model) < 0)
        || (resources_get_int("CIA1Model", &cia1_model) < 0)
        || (resources_get_int("CIA2Model", &cia2_model) < 0)
        || (resources_get_int("VICIINewLuminances", &new_luma) < 0)
        || (resources_get_int("BoardType", &board) < 0)
        || (resources_get_int("IECReset", &iecreset) < 0)
        || (resources_get_string("KernalName", &kernal) < 0)
        || (resources_get_string("ChargenName", &chargen) < 0)) {
        return -1;
    }

    return c64model_get_temp(video, sid_model, 0,
                             cia1_model, cia2_model, new_luma, board, iecreset, 
                             kernal, chargen);
}

static void c64model_set_temp(int model, int *vicii_model, int *sid_model,
                       int *glue_logic, int *cia1_model, int *cia2_model,
                       int *new_luma, int *board, int *iecreset,
                       const char *kernal, const char *chargen)
{
    int old_model;
    int old_engine;
    int old_sid_model;
    int new_sid_model;
    int old_type;
    int new_type;

    old_model = c64model_get_temp(*vicii_model, *sid_model, *glue_logic,
                                  *cia1_model, *cia2_model, *new_luma, *board, *iecreset, kernal, chargen);

    if ((model == old_model) || (model == C64MODEL_UNKNOWN)) {
        return;
    }

    *vicii_model = c64models[model].video;
    *cia1_model = c64models[model].cia;
    *cia2_model = c64models[model].cia;
    *glue_logic = 0; /* unused in x64 */
    *new_luma = c64models[model].luma;
    *board = c64models[model].board;
    *iecreset = c64models[model].iecreset;

    /* Only change the SID model if the model changes from 6581 to 8580.
       This allows to switch between "pal"/"oldpal" without changing
       the specific SID model. The current engine is preserved. */
    old_engine = (*sid_model >> 8);
    old_sid_model = (*sid_model & 0xff);

    new_sid_model = c64models[model].sid;

    old_type = is_new_sid(old_sid_model);
    new_type = is_new_sid(new_sid_model);

    if (old_type != new_type) {
        *sid_model = (old_engine << 8 ) | new_sid_model;
    }
}

/* get details for model */
void c64model_set_details(c64model_details_t *details, int model)
{
    c64model_set_temp(model, &details->vicii_model, &details->sid_model,
                       &details->glue_logic, &details->cia1_model, &details->cia2_model,
                       &details->new_luma, &details->board, &details->iecreset, 
                       details->kernal, details->chargen);
}

void c64model_set(int model)
{
    int old_model;
    int old_engine;
    int old_sid_model;
    int old_type;
    int new_sid_model;
    int new_type;

    old_model = c64model_get();

    if ((model == old_model) || (model == C64MODEL_UNKNOWN)) {
        return;
    }

    resources_set_int("MachineVideoStandard", c64models[model].video);
    resources_set_int("CIA1Model", c64models[model].cia);
    resources_set_int("CIA2Model", c64models[model].cia);
    resources_set_int("VICIINewLuminances", c64models[model].luma);
    resources_set_int("BoardType", c64models[model].board);
    resources_set_int("IECReset", c64models[model].iecreset);

    resources_set_string("KernalName", c64models[model].kernalname);
    resources_set_string("ChargenName", c64models[model].chargenname);
    
    /* Only change the SID model if the model changes from 6581 to 8580.
       This allows to switch between "pal"/"oldpal" without changing
       the specific SID model. The current engine is preserved. */

    resources_get_int("SidEngine", &old_engine);
    resources_get_int("SidModel", &old_sid_model);
    new_sid_model = c64models[model].sid;

    old_type = is_new_sid(old_sid_model);
    new_type = is_new_sid(new_sid_model);

    if (old_type != new_type) {
        sid_set_engine_model(old_engine, new_sid_model);
    }
}
