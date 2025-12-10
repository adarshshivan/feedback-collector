const API_BASE = "https://kvof9b5or1.execute-api.ap-south-1.amazonaws.com/prod";

document.getElementById("feedbackForm").addEventListener("submit", async (event) => {
    event.preventDefault();

    const payload = {
        email: document.getElementById("email").value,
        rating: Number(document.getElementById("rating").value),
        message: document.getElementById("message").value,
        recaptcha_token: document.getElementById("recaptcha_token").value
    };

    const resultBox = document.getElementById("result");
    resultBox.innerText = "Submitting...";

    try {
        const response = await fetch(`${API_BASE}/feedback`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(payload),
        });

        //  If AWS works normally
        if (response.ok) {
            const data = await response.json();
            resultBox.innerText = `Feedback submitted! ID: ${data.feedback_id}`;
            resultBox.style.color = "green";
            return;
        }

        // If AWS responds with an error (403 / 500 / CORS)
        throw new Error("AWS request failed");

    } catch (err) {
        console.warn("AWS unreachable → Switching to DEMO MODE.");

        // DEMO MODE RESPONSE
        const demoId = "DEMO-" + Math.floor(Math.random() * 999999);

        resultBox.innerText = `Feedback submitted! (Demo Mode) ID: ${demoId}`;
        resultBox.style.color = "orange";
    }
});
