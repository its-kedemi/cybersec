
import streamlit as st

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Cybersecurity Awareness Test",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# --------------------------------------------------
# STREAMLIT PAGE STYLING
# --------------------------------------------------

st.markdown(
    """
    <style>
        #MainMenu,
        footer,
        header,
        [data-testid="stToolbar"] {
            visibility: hidden;
        }

        .stApp {
            background: #020806;
        }

        .block-container {
            padding: 0 !important;
            max-width: 100% !important;
        }

        iframe {
            border: none !important;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# --------------------------------------------------
# HTML, CSS AND JAVASCRIPT
# --------------------------------------------------

html_content = r"""
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">

    <meta
        name="viewport"
        content="width=device-width, initial-scale=1.0"
    >

    <title>Cybersecurity Awareness Test</title>

    <style>

        * {
            box-sizing: border-box;
        }

        html,
        body {
            margin: 0;
            padding: 0;
            width: 100%;
            min-height: 100%;
            background: #020806;
            color: #e8fff1;
            font-family: Arial, Helvetica, sans-serif;
            overflow: hidden;
        }

        /* MAIN SCREEN */

        .screen {
            position: relative;
            min-height: 740px;
            height: 100vh;
            width: 100%;

            display: flex;
            align-items: center;
            justify-content: center;

            overflow: hidden;

            background:
                radial-gradient(
                    ellipse at center,
                    #07351d 0%,
                    #020c07 48%,
                    #000000 100%
                );
        }

        /* MATRIX BACKGROUND */

        canvas {
            position: absolute;
            inset: 0;

            width: 100%;
            height: 100%;

            opacity: 0.75;
        }

        /* CONTENT CONTAINER */

        .overlay {
            position: relative;
            z-index: 2;

            width: min(90%, 760px);

            padding: 35px 24px;

            text-align: center;

            border: 1px solid rgba(48,255,126,0.3);

            border-radius: 20px;

            background: rgba(0,10,5,0.90);

            box-shadow:
                0 0 65px rgba(0,255,100,0.12);

            backdrop-filter: blur(6px);

            animation: appear 1s ease both;
        }

        /* INTRODUCTION */

        .initial {
            color: #54ff98;

            font-size: 15px;

            letter-spacing: 3px;

            animation: pulse 1.5s infinite;
        }

        /* REVEAL CONTENT */

        .hidden {
            display: none;
        }

        .tag {
            color: #54ff98;

            font-size: 12px;

            letter-spacing: 4px;

            font-weight: bold;

            margin-bottom: 28px;
        }

        .shield {
            font-size: 45px;

            margin-bottom: 14px;

            filter:
                drop-shadow(0 0 16px #19ff79);
        }

        h1 {
            color: #68ff9d;

            font-size: clamp(28px, 5vw, 54px);

            line-height: 1.15;

            margin: 0 0 18px;

            text-shadow:
                0 0 25px rgba(40,255,120,0.4);
        }

        .subtitle {
            color: #d4ffe1;

            font-size: clamp(15px, 2.2vw, 19px);

            line-height: 1.7;

            margin: 0 auto 25px;

            max-width: 570px;
        }

        /* DIVIDER */

        .divider {
            height: 1px;

            background:
                linear-gradient(
                    90deg,
                    transparent,
                    #29ff80,
                    transparent
                );

            margin: 24px 0;
        }

        /* LESSON */

        .lesson {
            text-align: left;

            color: #d5e8dc;

            font-size: 15px;

            line-height: 1.7;
        }

        .lesson h2 {
            color: #64ff9b;

            font-size: 17px;

            margin-bottom: 12px;
        }

        .lesson ul {
            padding-left: 23px;

            margin-bottom: 0;
        }

        .lesson li {
            margin: 8px 0;
        }

        /* FOOTER MESSAGE */

        .notice {
            margin-top: 24px;

            font-size: 12px;

            color: #84a995;

            letter-spacing: 1px;
        }

        /* ANIMATIONS */

        @keyframes appear {

            from {
                opacity: 0;
                transform: translateY(12px);
            }

            to {
                opacity: 1;
                transform: translateY(0);
            }

        }

        @keyframes pulse {

            0%, 100% {
                opacity: 1;
            }

            50% {
                opacity: 0.4;
            }

        }

        /* MOBILE RESPONSIVENESS */

        @media(max-width: 520px) {

            .screen {
                min-height: 740px;
            }

            .overlay {
                padding: 28px 20px;
            }

            .tag {
                letter-spacing: 2px;
            }

        }

        @media(prefers-reduced-motion: reduce) {

            .overlay,
            .initial {
                animation: none;
            }

        }

    </style>

</head>

<body>

    <main class="screen">

        <!-- ANIMATED BACKGROUND -->

        <canvas
            id="matrix"
            aria-hidden="true">
        </canvas>

        <!-- MAIN CONTENT -->

        <section
            class="overlay"
            aria-live="polite">

            <!-- INTRO SCREEN -->

            <div
                class="initial"
                id="intro">

                INITIALISING SECURITY AWARENESS...

            </div>

            <!-- FINAL REVEAL -->

            <div
                id="reveal"
                class="hidden">

                <div class="tag">
                    CYBERSECURITY AWARENESS
                </div>

                <div
                    class="shield"
                    aria-hidden="true">

                    🛡️

                </div>

                <h1>
                    THIS IS A PHISHING TEST
                </h1>

                <p class="subtitle">

                    You have just experienced a simulated
                    phishing exercise.

                    This page is part of a cybersecurity
                    awareness presentation.

                    No passwords or sensitive information
                    were requested here.

                </p>

                <div class="divider"></div>

                <!-- SECURITY LESSON -->

                <div class="lesson">

                    <h2>
                        What should you look for next time?
                    </h2>

                    <ul>

                        <li>
                            <strong>Verify the sender:</strong>
                            Check the complete email address
                            and domain.
                        </li>

                        <li>
                            <strong>Check the context:</strong>
                            Were you expecting this Odoo inquiry
                            or request?
                        </li>

                        <li>
                            <strong>Inspect links:</strong>
                            Confirm the destination before
                            opening it.
                        </li>

                        <li>
                            <strong>Verify independently:</strong>
                            Contact the sender through a
                            trusted channel.
                        </li>

                        <li>
                            <strong>Report suspicious messages:</strong>
                            Use your organisation's approved
                            reporting process.
                        </li>

                    </ul>

                </div>

                <div class="notice">

                    SECURITY IS EVERYONE'S RESPONSIBILITY

                    <br>

                    LEARN · VERIFY · REPORT

                </div>

            </div>

        </section>

    </main>

    <!-- MATRIX ANIMATION SCRIPT -->

    <script>

        (() => {

            const canvas =
                document.getElementById("matrix");

            const ctx =
                canvas.getContext("2d");

            const intro =
                document.getElementById("intro");

            const reveal =
                document.getElementById("reveal");

            let width;
            let height;
            let columns;
            let drops;

            const fontSize = 16;

            // RESIZE CANVAS

            function resize() {

                const rect =
                    canvas.getBoundingClientRect();

                const dpr =
                    Math.min(
                        window.devicePixelRatio || 1,
                        2
                    );

                width = rect.width;
                height = rect.height;

                canvas.width = width * dpr;
                canvas.height = height * dpr;

                ctx.setTransform(
                    dpr,
                    0,
                    0,
                    dpr,
                    0,
                    0
                );

                columns =
                    Math.ceil(width / fontSize);

                drops = Array.from(
                    { length: columns },
                    () => Math.random() *
                        (-height / fontSize)
                );

            }

            // DRAW MATRIX EFFECT

            function draw() {

                ctx.fillStyle =
                    "rgba(0,8,4,0.12)";

                ctx.fillRect(
                    0,
                    0,
                    width,
                    height
                );

                ctx.font =
                    fontSize + "px monospace";

                for (
                    let i = 0;
                    i < drops.length;
                    i++
                ) {

                    ctx.fillStyle =
                        Math.random() > 0.94
                        ? "#d5ffe2"
                        : "#20ff72";

                    const character =
                        Math.random() > 0.5
                        ? "1"
                        : "0";

                    ctx.fillText(
                        character,
                        i * fontSize,
                        drops[i] * fontSize
                    );

                    if (
                        drops[i] * fontSize > height &&
                        Math.random() > 0.975
                    ) {

                        drops[i] = 0;

                    }

                    drops[i] +=
                        0.7 + Math.random() * 0.8;

                }

                requestAnimationFrame(draw);

            }

            // START ANIMATION

            resize();

            draw();

            window.addEventListener(
                "resize",
                resize
            );

            // REVEAL AWARENESS MESSAGE

            setTimeout(() => {

                intro.classList.add("hidden");

                reveal.classList.remove("hidden");

            }, 2800);

        })();

    </script>

</body>

</html>
"""

# --------------------------------------------------
# RENDER HTML
# --------------------------------------------------

st.html(html_content)
