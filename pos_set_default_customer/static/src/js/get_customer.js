import { patch } from "@web/core/utils/patch";
import { PosOrder } from "@point_of_sale/app/models/pos_order";

patch(PosOrder.prototype, {
    setup(vals, models) {
        super.setup(vals, models);
        const config = this.pos?.config;
        if (config?.default_partner_id && !this.partner_id) {
            const partner = this.pos.models["res.partner"].get(config.default_partner_id);
            if (partner) {
                this.partner_id = partner;
            }
        }
    },
});
