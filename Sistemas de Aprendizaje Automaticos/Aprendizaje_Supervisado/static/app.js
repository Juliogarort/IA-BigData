"use strict";

/* ── Referencias al DOM ─────────────────────────────────────── */
const canvas  = document.getElementById('drawCanvas');
const ctx     = canvas.getContext('2d');
const hint    = document.getElementById('canvasHint');
const wrapper = canvas.closest('.canvas-wrapper');

/* Estado del dibujo */
let dibujando = false;
let hasDrawn  = false;


ctx.fillStyle = '#000000';
ctx.fillRect(0, 0, canvas.width, canvas.height);


ctx.strokeStyle = '#ffffff';
ctx.lineWidth   = 18;
ctx.lineCap     = 'round';   
ctx.lineJoin    = 'round';


function getPos(e) {
    const rect   = canvas.getBoundingClientRect();
    const scaleX = canvas.width  / rect.width;
    const scaleY = canvas.height / rect.height;
    const src    = e.touches ? e.touches[0] : e;
    return {
        x: (src.clientX - rect.left) * scaleX,
        y: (src.clientY - rect.top)  * scaleY
    };
}

/* ── Handlers de dibujo ─────────────────────────────────────── */
function startDraw(e) {
    dibujando = true;

    if (!hasDrawn) {
        hasDrawn = true;
        hint.classList.add('hidden');
    }
    wrapper.classList.add('drawing');

    const p = getPos(e);
    ctx.beginPath();
    ctx.moveTo(p.x, p.y);
}

function draw(e) {
    if (!dibujando) return;
    const p = getPos(e);
    ctx.lineTo(p.x, p.y);
    ctx.stroke();
}

function stopDraw() {
    dibujando = false;
}

/*  eventos de ratón y táctiles */
canvas.addEventListener('mousedown',  startDraw);
canvas.addEventListener('mousemove',  draw);
canvas.addEventListener('mouseup',    stopDraw);
canvas.addEventListener('mouseleave', stopDraw);
canvas.addEventListener('touchstart', e => { e.preventDefault(); startDraw(e); }, { passive: false });
canvas.addEventListener('touchmove',  e => { e.preventDefault(); draw(e);      }, { passive: false });
canvas.addEventListener('touchend',   stopDraw);

/* ── Función borrar ─────────────────────────────────────────── */
function borrar() {
    ctx.fillStyle = '#000000';
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    hasDrawn = false;
    hint.classList.remove('hidden');
    wrapper.classList.remove('drawing');

    const box = document.getElementById('resultBox');
    box.className = 'result';
    box.innerHTML = `
        <div class="result-empty">
            <span class="result-empty-char">?</span>
            <span class="result-empty-label">sin predicción</span>
        </div>`;
}


function preprocesar() {
    const W = canvas.width;   
    const H = canvas.height;  

    const raw = ctx.getImageData(0, 0, W, H).data;

    const UMBRAL = 30;
    const gray   = new Float32Array(W * H);
    for (let i = 0; i < W * H; i++) {
        const r = raw[i * 4];
        gray[i] = (r < UMBRAL) ? 0 : r;
    }

    let minX = W, maxX = -1, minY = H, maxY = -1;
    for (let y = 0; y < H; y++) {
        for (let x = 0; x < W; x++) {
            if (gray[y * W + x] > 0) {
                if (x < minX) minX = x;
                if (x > maxX) maxX = x;
                if (y < minY) minY = y;
                if (y > maxY) maxY = y;
            }
        }
    }

    if (maxX < 0) return new Array(64).fill(0);

    const bboxW = maxX - minX;
    const bboxH = maxY - minY;
    const pad   = Math.round(Math.max(bboxW, bboxH) * 0.15);
    const x0 = Math.max(0, minX - pad);
    const y0 = Math.max(0, minY - pad);
    const x1 = Math.min(W, maxX + pad + 1);
    const y1 = Math.min(H, maxY + pad + 1);
    const cW = x1 - x0;
    const cH = y1 - y0;

    const side = Math.max(cW, cH);
    const offX = Math.round((side - cW) / 2);
    const offY = Math.round((side - cH) / 2);

    const tmp  = document.createElement('canvas');
    tmp.width  = side;
    tmp.height = side;
    const tCtx = tmp.getContext('2d');
    tCtx.fillStyle = '#000000';
    tCtx.fillRect(0, 0, side, side);
    tCtx.drawImage(canvas, x0, y0, cW, cH, offX, offY, cW, cH);

    const small  = document.createElement('canvas');
    small.width  = 8;
    small.height = 8;
    const sCtx   = small.getContext('2d');
    sCtx.imageSmoothingEnabled = true;
    sCtx.imageSmoothingQuality = 'high';
    sCtx.drawImage(tmp, 0, 0, 8, 8);

    const pixels = sCtx.getImageData(0, 0, 8, 8).data;
    const flat   = new Array(64);
    let maxVal   = 0;

    for (let i = 0; i < 64; i++) {
        const v = Math.max(0, pixels[i * 4]);
        flat[i] = v;
        if (v > maxVal) maxVal = v;
    }

    if (maxVal > 0) {
        const scale = 16.0 / maxVal;
        for (let i = 0; i < 64; i++) flat[i] *= scale;
    }

    return flat;
}

/* ── Función predecir ───────────────────────────────────────── */
async function predecir() {
    const box = document.getElementById('resultBox');

    box.className = 'result';
    box.innerHTML = `
        <div class="analyzing">
            <span>analizando</span>
            <div class="dots"><span></span><span></span><span></span></div>
        </div>`;

    const pixelData = preprocesar();

    try {
        const res  = await fetch('/predict', {
            method:  'POST',
            headers: { 'Content-Type': 'application/json' },
            body:    JSON.stringify({ pixels: pixelData })
        });

        const data = await res.json();
        if (data.error) throw new Error(data.error);

        const pct = data.confidence;
        box.className = 'result active';
        box.innerHTML = `
            <div class="result-left">
                <span class="result-tag">predicción</span>
                <span class="result-digit">${data.prediction}</span>
            </div>
            <div class="result-right">
                <span class="conf-label">confianza</span>
                <span class="conf-value">${pct}%</span>
                <div class="conf-bar-track">
                    <div class="conf-bar-fill" id="confBar"></div>
                </div>
            </div>`;

        requestAnimationFrame(() => {
            const bar = document.getElementById('confBar');
            if (bar) bar.style.width = Math.min(pct, 100) + '%';
        });

    } catch (err) {
        box.className = 'result';
        box.innerHTML = `
            <div class="result-empty">
                <span class="result-empty-char" style="font-size:1.5rem; color:#ff4444">!</span>
                <span class="result-empty-label">${err.message}</span>
            </div>`;
    }
}