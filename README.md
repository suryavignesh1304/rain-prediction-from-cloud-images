    <h1>Cloud Rain Prediction Model</h1>
    <p>
        This project uses a Convolutional Neural Network (CNN) model to predict the likelihood of rain based on cloud images. 
        The model is trained on cloud types and classifies them into rain-likely or non-rain-likely categories.
    </p>

    <h2>Features</h2>
    <ul>
        <li>Classification of clouds into rain-likely (Ns, St, Sc) and non-rain-likely types.</li>
        <li>Pre-trained model stored as <code>cloud_rain_predictor.h5</code>.</li>
        <li>Deployed Streamlit app for real-time predictions.</li>
    </ul>

    <h2>Deployed App</h2>
    <p>
        Access the deployed app here: 
        <a href="https://weathervision.streamlit.app/" target="_blank">Cloud Rain Prediction App</a>
    </p>

    <h2>Dataset</h2>
    <p>
        The dataset consists of cloud images categorized into the following types:
    </p>
    <ul>
        <li>Altocumulus (Ac)</li>
        <li>Altostratus (As)</li>
        <li>Cirrocumulus (Cc)</li>
        <li>Cirrus (Ci)</li>
        <li>Cirrostratus (Cs)</li>
        <li>Cumulus (Cu)</li>
        <li>Nimbostratus (Ns)</li>
        <li>Stratus (St)</li>
        <li>Stratocumulus (Sc)</li>
    </ul>

    <h2>Model Architecture</h2>
    <p>The CNN model has the following architecture:</p>
    <ul>
        <li>3 Convolutional layers with ReLU activation and MaxPooling</li>
        <li>1 Fully connected dense layer</li>
        <li>Output layer with sigmoid activation</li>
    </ul>

    <h2>Usage</h2>
    <ol>
        <li>Clone the repository: <code>git clone https://github.com/your-repo/cloud-rain-predictor.git</code></li>
        <li>Install dependencies: <code>pip install -r requirements.txt</code></li>
        <li>Run the Streamlit app: <code>streamlit run app.py</code></li>
    </ol>

    <h2>Sample Outputs</h2>
    <h3>Deployed App Prediction</h3>
    <p>
        <img src="ouputsample/app.png/400x300" alt="Deployed App Screenshot">
    </p>

    <h3>Test Image Predictions</h3>
    <p>
        <strong>Input Image:</strong>
        <img src="ouputsample/input.jpg/128x128" alt="Sample Input Image">
    </p>
    <p>
        <strong>Prediction:</strong> No rain likely (Confidence: 0.80)
    </p>

    <h2>Model Performance</h2>
    <p>
        <strong>Test Accuracy:</strong> 90% <br>
        The model achieves high accuracy in distinguishing rain-likely clouds from other cloud types.
    </p>

    <h2>License</h2>
    <p>
        This project is licensed under the MIT License.
    </p>

    <h2>Contact</h2>
    <p>
        For any queries or contributions, feel free to reach out via GitHub issues or email.
    </p>
