import { patch } from "@web/core/utils/patch";
import { PosOrder } from "@point_of_sale/app/models/pos_order";
import { PosStore } from "@point_of_sale/app/services/pos_store";
import { PaymentScreen } from "@point_of_sale/app/screens/payment_screen/payment_screen";

// Load extra partner fields needed for AR invoice ticket
patch(PosStore.prototype, {
    async processServerData() {
        await super.processServerData();
        // Load afip responsibility type for general customer check
        if (!this._generalCustomerId && this.models["l10n_ar.afip.responsibility.type"]) {
            const cfType = this.models["l10n_ar.afip.responsibility.type"].find(
                (r) => r.code === "5"
            );
            this._generalCustomerId = cfType?.id;
        }
    },
    get generalCustomerId() {
        return this._generalCustomerId;
    },
});

// Auto-invoice and default partner logic
patch(PosOrder.prototype, {
    setup(vals, models) {
        super.setup(vals, models);
        const config = this.pos?.config;
        if (config?.pos_auto_invoice) {
            this.to_invoice = true;
        }
        if (config?.default_partner_id && !this.partner_id) {
            const partner = this.pos.models["res.partner"].get(config.default_partner_id);
            if (partner) {
                this.partner_id = partner;
            }
        }
    },
});

// On payment screen mount, auto-set invoice flag
patch(PaymentScreen.prototype, {
    onMounted() {
        super.onMounted();
        if (this.pos.config.pos_auto_invoice) {
            this.currentOrder.setToInvoice(true);
        }
    },
});
