const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const { exec } = require('child_process');

const app = express();
const PORT = process.env.PORT || 5001;

// Use CORS middleware to handle cross-origin requests
app.use(cors());
app.use(bodyParser.json());

app.post('/classify', (req, res) => {
    const { text } = req.body;

    // Log the received text to verify
    console.log(`Received text: ${text}`);

    // Execute the Python script classifier.py ml/classifieraiml.py nlp/classifiernlp.py
    exec(`python3 classifier.py "${text}"`, (error, stdout, stderr) => {
        if (error) {
            console.error(`Error: ${stderr}`);
            return res.status(500).send('Error processing text');
        }
        res.send(stdout.trim());
    });
});

app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});
