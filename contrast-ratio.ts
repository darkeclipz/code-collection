interface RGB {
    r: number;
    g: number;
    b: number;
}

// See https://www.w3.org/TR/WCAG20/ for more information.
export class ContrastRatio {

    // Converts a hex value, e.g.: #00ff00 to a normalized RGB triple [0, 1, 0].
    rgbHexToInt(hex: string): RGB {

        if (hex[0] != '#') {
            console.warn("Can't convert hex '" + hex + "' to integer, the hex should be prefixed with #.");
            return;
        }

        if (hex.length != 7) {
            console.warn("Hex color '" + hex + "' must be 7 characters.");
            return;
        }

        let r = '0x' + hex.substring(1, 3);
        let g = '0x' + hex.substring(3, 5);
        let b = '0x' + hex.substring(5, 7);

        return { r: parseInt(r) / 255, g: parseInt(g) / 255, b: parseInt(b) / 255 };

    }

    // Calculates the relative luminance for a normalized RGB triple.
    // Reference: https://www.w3.org/TR/WCAG20/#meaning
    relativeLuminance(rgb: RGB): number {

        let R = rgb.r <= 0.03928 ? rgb.r / 12.92 : Math.pow(((rgb.r + 0.055) / 1.055), 2.4);
        let G = rgb.g <= 0.03928 ? rgb.g / 12.92 : Math.pow(((rgb.g + 0.055) / 1.055), 2.4);
        let B = rgb.b <= 0.03928 ? rgb.b / 12.92 : Math.pow(((rgb.b + 0.055) / 1.055), 2.4);
        let L = 0.2126 * R + 0.7152 * G + 0.0722 * B;
        return L;

    }

    // Calculates the contrast ratio between two relative luminances, which is a value between [1, 21].
    // According to WCAG20, section 3.1, the contrast ratio should be atleast 4.5.
    // Reference: https://www.w3.org/TR/WCAG20/#meaning
    contrastRatioByLuminance(L1: number, L2: number) {

        // Make sure that L1 has the highest luminance, if L2 is higher,
        // we swap them.
        if (L2 > L1) {
            let swap = L2;
            L2 = L1;
            L1 = swap;
        }

        // Calculate the contrast ratio for the two relative luminances.
        let CR = (L1 + 0.05) / (L2 + 0.05);

        return CR;

    }

    // Calculates the contrast ratio for two RGB hex values.
    contrastRatioByHex(rgbHex1: string, rgbHex2: string): number {

        // Convert the hex color to normalized RGB vectors.
        let C1 = this.rgbHexToInt(rgbHex1);
        let C2 = this.rgbHexToInt(rgbHex2);

        // Calculate the relative luminance for the normalized RGB vectors.
        let L1 = this.relativeLuminance(C1);
        let L2 = this.relativeLuminance(C2);

        // Calculate the contrast ratio for the relative luminances.
        let CR = this.contrastRatioByLuminance(L1, L2);

        return CR;

    }

}