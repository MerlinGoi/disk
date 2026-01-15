  const chat = document.getElementById('chat');
  const form = document.getElementById('form');
  const input = document.getElementById('message');

  function appendMessage(text, who){
    const div = document.createElement('div');
    div.className = 'msg ' + who;
    const b = document.createElement('span');
    b.className = 'bubble';
    b.textContent = text;
    div.appendChild(b);
    chat.appendChild(div);
    chat.scrollTop = chat.scrollHeight;
  }

  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    const text = input.value.trim();
    if (!text) return;
    appendMessage(text, 'user');
    input.value = '';

    try {
      const res = await fetch('save_message.php', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: text })
      });

      if (!res.ok) throw new Error('Network response was not OK');
      const data = await res.json();
      if (data && data.reply) appendMessage(data.reply, 'bot');
      else appendMessage('No reply (server returned unexpected response)', 'bot');
    } catch (err) {
      appendMessage('Error: ' + err.message, 'bot');
    }
  });

  // Small helpful prompt examples
  appendMessage('Try: "hello", "time", "help", "bye"', 'bot');
