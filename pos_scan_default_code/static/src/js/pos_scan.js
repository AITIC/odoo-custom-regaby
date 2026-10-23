import { patch } from "@web/core/utils/patch";
import { ProductProduct } from "@point_of_sale/app/models/product_product";
import { normalize } from "@web/core/l10n/utils";

patch(ProductProduct.prototype, {
    get searchString() {
        const fields = ["display_name", "barcode", "default_code", "modelo_articulo"];
        const attributeValues = (this.product_template_attribute_value_ids || []).map(
            (v) => v.name
        );
        const raw = fields
            .map((field) => this[field] || "")
            .concat(attributeValues)
            .filter(Boolean)
            .join(" ");
        return normalize(raw);
    },
});
