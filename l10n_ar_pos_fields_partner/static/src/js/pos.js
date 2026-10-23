import { patch } from "@web/core/utils/patch";
import { PosStore } from "@point_of_sale/app/services/pos_store";

// Load l10n_ar partner fields and make them available in the POS
patch(PosStore.prototype, {
    async processServerData() {
        await super.processServerData();
        // Ensure AFIP responsibility types and identification types are indexed
        if (!this.responsabilityTypes) {
            this.responsabilityTypes = this.models["l10n_ar.afip.responsibility.type"]
                ? [...this.models["l10n_ar.afip.responsibility.type"].values()]
                : [];
        }
        if (!this.identificationTypes) {
            this.identificationTypes = this.models["l10n_latam.identification.type"]
                ? [...this.models["l10n_latam.identification.type"].values()]
                : [];
        }
    },
});
