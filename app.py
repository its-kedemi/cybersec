import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Cybersecurity Awareness Test",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
      #MainMenu, footer, header, [data-testid="stToolbar"] { visibility: hidden; }
      .stApp { background: #020806; }
      .block-container { padding: 0 !important; max-width: 100% !important; }
    </style>
    """,
    unsafe_allow_html=True,
)

components.html(
    """
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <style>
        * { box-sizing: border-box; }
        html, body { margin: 0; width: 100%; min-height: 100%; background: #020806;
          color: #e8fff1; font-family: Arial, Helvetica, sans-serif; overflow: hidden; }
        .screen { position: relative; min-height: 680px; height: 100vh; width: 100%;
          display: flex; align-items: center; justify-content: center; overflow: hidden;
          background: radial-gradient(ellipse at center, #07351d 0%, #020c07 48%, #000 100%); }
        canvas { position: absolute; inset: 0; width: 100%; height: 100%; opacity: .75; }
        .overlay { position: relative; z-index: 2; width: min(90%, 760px); padding: 35px 24px;
          text-align: center; border: 1px solid rgba(48,255,126,.3); border-radius: 20px;
          background: rgba(0,10,5,.88); box-shadow: 0 0 65px rgba(0,255,100,.12);
          backdrop-filter: blur(6px); animation: appear 1s ease both; }
        .tag { color: #54ff98; font-size: 12px; letter-spacing: 4px; font-weight: bold; margin-bottom: 28px; }
        .shield { font-size: 45px; margin-bottom: 14px; filter: drop-shadow(0 0 16px #19ff79); }
        h1 { color: #68ff9d; font-size: clamp(28px,5vw,54px); line-height: 1.15; margin: 0 0 18px;
          text-shadow: 0 0 25px rgba(40,255,120,.4); }
        .subtitle { color: #d4ffe1; font-size: clamp(15px,2.2vw,19px); line-height: 1.7;
          margin: 0 auto 25px; max-width: 570px; }
        .divider { height: 1px; background: linear-gradient(90deg,transparent,#29ff80,transparent); margin: 24px 0; }
        .lesson { text-align: left; color: #d5e8dc; font-size: 15px; line-height: 1.7; }
        .lesson h2 { color: #64ff9b; font-size: 17px; margin-bottom: 12px; }
        .lesson ul { padding-left: 23px; margin-bottom: 0; }
        .lesson li { margin: 8px 0; }
        .notice { margin-top: 24px; font-size: 12px; color: #84a995; letter-spacing: 1px; }
        .initial { color: #54ff98; font-size: 15px; letter-spacing: 3px; }
        .hidden { display: none; }
        @keyframes appear { from { opacity: 0; transform: translateY(12px); } to { opacity: 1; transform: translateY(0); } }
        @media(max-width:520px) { .screen { min-height: 720px; } .overlay { padding: 28px 20px; } .tag { letter-spacing: 2px; } }
        @media(prefers-reduced-motion:reduce) { .overlay { animation: none; } }
      </style>
    </head>
    <body>
      <main class="screen">
        <canvas id="matrix" aria-hidden="true"></canvas>
        <section class="overlay" aria-live="polite">
          <div class="initial" id="intro">INITIALISING SECURITY AWARENESS...</div>
          <div id="reveal" class="hidden">
            <div class="tag">CYBERSECURITY AWARENESS</div>
            <div class="shield" aria-hidden="true">🛡️</div>
            <h1>THIS IS A PHISHING TEST</h1>
            <p class="subtitle">You have just experienced a simulated phishing exercise.
              This page is part of a cybersecurity awareness presentation.
              No passwords or sensitive information were requested here.</p>
            <div class="divider"></div>
            <div class="lesson">
              <h2>What should you look for next time?</h2>
              <ul>
                <li><strong>Verify the sender:</strong> check the complete email address and domain.</li>
                <li><strong>Check the context:</strong> were you expecting this Odoo inquiry or request?</li>
                <li><strong>Inspect links:</strong> confirm the destination before opening it.</li>
                <li><strong>Verify independently:</strong> contact the sender through a trusted channel.</li>
                <li><strong>Report suspicious messages:</strong> use your organisation's approved reporting process.</li>
              </ul>
            </div>
            <div class="notice">SECURITY IS EVERYONE'S RESPONSIBILITY · LEARN, VERIFY, REPORT</div>
          </div>
        </section>
      </main>
      <script>
        (() => {
          const canvas = document.getElementById("matrix");
          const ctx = canvas.getContext("2d");
          const intro = document.getElementById("intro");
          const reveal = document.getElementById("reveal");
          let width, height, columns, drops;
          const fontSize = 16;
          function resize() {
            const rect = canvas.getBoundingClientRect();
            const dpr = Math.min(window.devicePixelRatio || 1, 2);
            width = rect.width; height = rect.height;
            canvas.width = width * dpr; canvas.height = height * dpr;
            ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
            columns = Math.ceil(width / fontSize);
            drops = Array.from({length: columns}, () => Math.random() * -height / fontSize);
          }
          function draw() {
            ctx.fillStyle = "rgba(0,8,4,.12)";
            ctx.fillRect(0, 0, width, height);
            ctx.font = fontSize + "px monospace";
            for (let i = 0; i < drops.length; i++) {
              ctx.fillStyle = Math.random() > .94 ? "#d5ffe2" : "#20ff72";
              ctx.fillText(Math.random() > .5 ? "1" : "0", i * fontSize, drops[i] * fontSize);
              if (drops[i] * fontSize > height && Math.random() > .975) drops[i] = 0;
              drops[i] += .7 + Math.random() * .8;
            }
            requestAnimationFrame(draw);
          }
          resize(); draw();
          window.addEventListener("resize", resize);
          setTimeout(() => { intro.classList.add("hidden"); reveal.classList.remove("hidden"); }, 2800);
        })();
      </script>
    </body>
    </html>
    """,
    height=740,
    scrolling=False,
)
