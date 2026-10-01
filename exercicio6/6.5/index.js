const express = require('express');
const app = express();
app.get('/', (req, res) => res.send('Salvei.'));
app.listen(3000, () => console.log('Servidor na port 3000'));