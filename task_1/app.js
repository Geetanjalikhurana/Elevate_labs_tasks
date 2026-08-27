document.addEventListener('DOMContentLoaded', () => {
    const mainDisplay = document.getElementById('mainDisplay');
    const expressionDisplay = document.getElementById('expressionDisplay');
    const historyList = document.getElementById('historyList');
    const clearHistoryBtn = document.getElementById('clearHistoryBtn');

    let currentInput = '0';
    let previousInput = '';
    let operator = null;
    let shouldResetDisplay = false;
    let history = [];

    // Handle number input
    function appendNumber(number) {
        if (currentInput === '0' || shouldResetDisplay) {
            currentInput = number === '.' ? '0.' : number;
            shouldResetDisplay = false;
        } else {
            if (number === '.' && currentInput.includes('.')) return;
            currentInput += number;
        }
        updateDisplay();
    }

    // Handle operator selection
    function handleOperator(op) {
        if (operator !== null && !shouldResetDisplay) {
            calculate();
        }
        previousInput = currentInput;
        operator = op;
        shouldResetDisplay = true;
        updateDisplay();
    }

    // Mathematical Operations
    function calculate() {
        if (operator === null || shouldResetDisplay) return;

        const prev = parseFloat(previousInput);
        const current = parseFloat(currentInput);

        if (isNaN(prev) || isNaN(current)) return;

        let result = 0;
        let opSymbol = operator;

        switch (operator) {
            case '+':
                result = prev + current;
                break;
            case '-':
                result = prev - current;
                break;
            case '*':
                result = prev * current;
                opSymbol = '×';
                break;
            case '/':
                if (current === 0) {
                    alert('Error: Division by zero is not allowed!');
                    clear();
                    return;
                }
                result = prev / current;
                opSymbol = '÷';
                break;
            case '^':
                result = Math.pow(prev, current);
                break;
            case '%':
                if (current === 0) {
                    alert('Error: Modulus by zero is not allowed!');
                    clear();
                    return;
                }
                result = prev % current;
                break;
            default:
                return;
        }

        // Format result float/int
        const formattedResult = Number.isInteger(result) ? result.toString() : result.toFixed(4).replace(/\.?0+$/, '');

        // Add to history
        const historyItem = {
            expr: `${previousInput} ${opSymbol} ${currentInput}`,
            res: formattedResult
        };
        history.unshift(historyItem);
        renderHistory();

        currentInput = formattedResult;
        operator = null;
        previousInput = '';
        shouldResetDisplay = true;
        updateDisplay();
    }

    function clear() {
        currentInput = '0';
        previousInput = '';
        operator = null;
        shouldResetDisplay = false;
        updateDisplay();
    }

    function backspace() {
        if (shouldResetDisplay) return;
        if (currentInput.length === 1 || (currentInput.length === 2 && currentInput.startsWith('-'))) {
            currentInput = '0';
        } else {
            currentInput = currentInput.slice(0, -1);
        }
        updateDisplay();
    }

    function updateDisplay() {
        mainDisplay.textContent = currentInput;
        if (operator !== null) {
            let displayOp = operator;
            if (operator === '*') displayOp = '×';
            if (operator === '/') displayOp = '÷';
            expressionDisplay.textContent = `${previousInput} ${displayOp}`;
        } else {
            expressionDisplay.textContent = '';
        }
    }

    function renderHistory() {
        if (history.length === 0) {
            historyList.innerHTML = '<div class="empty-history">No calculations performed yet.</div>';
            return;
        }

        historyList.innerHTML = history.map(item => `
            <div class="history-item" onclick="useHistoryResult('${item.res}')">
                <div class="history-expr">${item.expr} =</div>
                <div class="history-res">${item.res}</div>
            </div>
        `).join('');
    }

    window.useHistoryResult = (val) => {
        currentInput = val;
        shouldResetDisplay = false;
        updateDisplay();
    };

    clearHistoryBtn.addEventListener('click', () => {
        history = [];
        renderHistory();
    });

    // Keypad Click Listeners
    document.querySelectorAll('.btn').forEach(button => {
        button.addEventListener('click', () => {
            const num = button.dataset.num;
            const op = button.dataset.op;
            const action = button.dataset.action;

            if (num !== undefined) appendNumber(num);
            if (op !== undefined) handleOperator(op);
            if (action === 'clear') clear();
            if (action === 'backspace') backspace();
            if (action === 'equals') calculate();
        });
    });

    // Keyboard support
    document.addEventListener('keydown', (e) => {
        if (e.key >= '0' && e.key <= '9') appendNumber(e.key);
        if (e.key === '.') appendNumber('.');
        if (e.key === '+') handleOperator('+');
        if (e.key === '-') handleOperator('-');
        if (e.key === '*') handleOperator('*');
        if (e.key === '/') {
            e.preventDefault();
            handleOperator('/');
        }
        if (e.key === '%') handleOperator('%');
        if (e.key === '^') handleOperator('^');
        if (e.key === 'Enter' || e.key === '=') {
            e.preventDefault();
            calculate();
        }
        if (e.key === 'Backspace') backspace();
        if (e.key === 'Escape') clear();
    });
});
