(function () {
    function detectBaseFromString(s) {
        if (/^0b[01]+$/i.test(s)) return 2;
        if (/^0x[0-9a-f]+$/i.test(s)) return 16;
        if (/^0o[0-7]+$/i.test(s)) return 8;
        if (/^[01]+$/.test(s)) return 2;   // -> binary 
        if (/^[0-9]+$/.test(s)) return 10;  // - > decimal
        if (/^[0-7]+$/.test(s)) return 8; 
        return null;
    }

    function parseBigIntWithBase(s, base) {
        
        s = String(s).trim();
        if (s === '') throw new Error('empty input');

        const sign = s.startsWith('-') ? '-' : '';
        const digits = s.replace(/^[+-]/, '');

        if (base === 10) {
            return BigInt(sign + digits);
        } else if (base === 2) {
            return BigInt(sign + '0b' + digits);
        } else if (base === 8) {
            return BigInt(sign + '0o' + digits);
        } else if (base === 16) {
            return BigInt(sign + '0x' + digits);
        } else {
            throw new Error('unsupported base');
        }
    }

    function formatBigInt(n) {
        const sign = n < 0n ? '-' : '';
        const abs = n < 0n ? -n : n;
        return {
            binary: sign + abs.toString(2),
            decimal: sign + abs.toString(10),
            hex: sign + '0x' + abs.toString(16).toUpperCase(),
            octal: sign + '0o' + abs.toString(8)
        };
    }


    const form = document.getElementById('base-form');
    const input = document.getElementById('integer-input');
    const result = document.getElementById('result');

    function showError(msg) {
        result.textContent = 'Error: ' + msg;
        result.style.color = 'crimson';
    }

    function showResult(r) {
        result.style.color = '';
        result.innerHTML = [
            `<div>Detected input base: <strong>${r.detectedBase ?? 'unknown'}</strong></div>`,
            `<div>Binary: ${r.binary}</div>`,
            `<div>Decimal: ${r.decimal}</div>`,
            `<div>Hex: ${r.hex}</div>`,
            `<div>Octal: ${r.octal}</div>`
        ].join('');
    }

    function convertAndShow() {
        const s = input.value.trim();
        if (s === '') { showError('please enter a number'); return; }

        const detectedFromString = detectBaseFromString(s);
        const effectiveBase = detectedFromString ?? 10;

        try {
            const n = parseBigIntWithBase(s, effectiveBase);
            const formatted = formatBigInt(n);
            showResult({ detectedBase: effectiveBase, ...formatted });
        } catch (err) {
            showError(err.message);
        }
    }

    form.addEventListener('submit', function (e) { e.preventDefault(); convertAndShow(); });
    input.addEventListener('input', convertAndShow);

})();