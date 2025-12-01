/* Compute nth Fibonacci number (n >= 0). Uses iterative approach with BigInt. */
function fibonacci(n) {
	if (!Number.isInteger(n) || n < 0) throw new RangeError('n must be a non-negative integer');
	if (n === 0) return 0n;
	if (n === 1) return 1n;
	let a = 0n, b = 1n;
	for (let i = 2; i <= n; i++) {
		const c = a + b;
		a = b;
		b = c;
	}
	return b;
}

/* Return an array of the first `count` Fibonacci numbers (count >= 0). */
function fibonacciSequence(count) {
	if (!Number.isInteger(count) || count < 0) throw new RangeError('count must be a non-negative integer');
	const out = [];
	for (let i = 1; i < count+2; i++) out.push(fibonacci(i));
	return out.map((value, index) => `to jest element numer: ${String(index)}- ${value}`);
}

console.log(fibonacciSequence(15).map(x => x.toString()));
console.log(fibonacci(1000));