    // Helpers
    const $ = (q) => document.querySelector(q);

    // 1) Compatibility range -> bar + value
    const range = $("#compatRange"), fill = $("#compatFill"), val = $("#compatVal");
    if (range && fill && val){
    const sync = () => { val.textContent = range.value; fill.style.width = range.value + "%"; };
    range.addEventListener("input", sync); sync();
    }

    // 2) Love Notes – localStorage
    const loveKey = "hih_love_note";
    const loveText = $("#loveText");
    const savedHint = $("#loveSaved");
    const saveLove = $("#saveLove");
    const clearLove = $("#clearLove");

    if (loveText){
    // load
    const prev = localStorage.getItem(loveKey);
    if (prev) loveText.value = prev;
    // save
    saveLove?.addEventListener("click", () => {
        localStorage.setItem(loveKey, loveText.value.trim());
        if (savedHint){ savedHint.hidden = false; setTimeout(()=> savedHint.hidden = true, 1200); }
    });
    // clear
    clearLove?.addEventListener("click", () => {
        loveText.value = ""; localStorage.removeItem(loveKey);
    });
    }

    // 3) Songs list – chips with remove
    const songInput = $("#songInput");
    const songList = $("#songList");
    $("#addSong")?.addEventListener("click", () => {
    const v = (songInput.value || "").trim();
    if (!v) return;
    const li = document.createElement("li");
    const a = document.createElement("a");
    a.href = v.startsWith("http") ? v : "#"; a.textContent = v; a.target = "_blank";
    li.append(a);
    const x = document.createElement("button"); x.textContent = "✕";
    x.addEventListener("click", ()=> li.remove());
    li.append(x);
    songList.append(li);
    songInput.value = "";
    });

    // 4) Destinations – toggle active
    document.querySelectorAll("#destChips .chip").forEach(chip=>{
    chip.addEventListener("click",()=> chip.classList.toggle("active"));
    });

    // 5) Pledge – preview + save (localStorage)
    const pledgeNames = $("#pledgeNames"), pledgeText = $("#pledgeText"), savePledge = $("#savePledge");
    const pledgePrev = $("#pledgePreview"), ppNames = $("#ppNames"), ppText = $("#ppText");
    const pledgeKey = "hih_pledge";

    const loadPledge = () => {
    const data = JSON.parse(localStorage.getItem(pledgeKey) || "{}");
    if (data.names || data.text){
        ppNames.textContent = data.names || "";
        ppText.textContent = data.text || "";
        pledgePrev.hidden = false;
    }
    };
    loadPledge();

    savePledge?.addEventListener("click", ()=>{
    const data = { names: (pledgeNames.value||"").trim(), text: (pledgeText.value||"").trim() };
    ppNames.textContent = data.names; ppText.textContent = data.text;
    pledgePrev.hidden = !(data.names || data.text);
    localStorage.setItem(pledgeKey, JSON.stringify(data));
    });

    // 6) Movies list
const movieInput = $("#movieInput");
const movieList = $("#movieList");
$("#addMovie")?.addEventListener("click", () => {
  const v = (movieInput.value || "").trim();
  if (!v) return;
  const li = document.createElement("li");
  li.textContent = v;
  const x = document.createElement("button"); x.textContent = "✕";
  x.addEventListener("click", ()=> li.remove());
  li.append(x);
  movieList.append(li);
  movieInput.value = "";
});

// 7) Anniversary countdown
const anniDate = $("#anniDate"), anniResult = $("#anniResult");
anniDate?.addEventListener("change", () => {
  const d = new Date(anniDate.value);
  if (!isNaN(d)) {
    const today = new Date();
    const diff = Math.ceil((d - today)/(1000*60*60*24));
    anniResult.textContent = diff >= 0 ? `${diff} days left ❤️` : `Already passed!`;
  }
});

// 8) Home style chips
document.querySelectorAll("#homeChips .chip").forEach(chip=>{
  chip.addEventListener("click",()=> chip.classList.toggle("active"));
});

// 9) Pet wishlist chips
document.querySelectorAll("#petChips .chip").forEach(chip=>{
  chip.addEventListener("click",()=> chip.classList.toggle("active"));
});

// 10) Memory Gallery
const imgInput = $("#imgInput"), imgGallery = $("#imgGallery");
$("#addImg")?.addEventListener("click", () => {
  const v = (imgInput.value || "").trim();
  if (!v) return;
  const img = document.createElement("img");
  img.src = v; img.style.width = "80px"; img.style.height = "80px"; img.style.borderRadius="10px"; img.style.objectFit="cover";
  imgGallery.append(img);
  imgInput.value = "";
});

// 11) Special Dates Reminder
const dateTitle = $("#dateTitle"), dateInput = $("#dateInput"), dateList = $("#dateList");
$("#addDate")?.addEventListener("click", () => {
  const title = (dateTitle.value || "").trim();
  const d = new Date(dateInput.value);
  if (!title || isNaN(d)) return;
  const li = document.createElement("li");
  const today = new Date();
  const diff = Math.ceil((d - today)/(1000*60*60*24));
  li.textContent = `${title}: ${d.toDateString()} (${diff >= 0 ? diff + " days left" : "passed"})`;
  const x = document.createElement("button"); x.textContent = "✕";
  x.addEventListener("click", ()=> li.remove());
  li.append(x);
  dateList.append(li);
  dateTitle.value = ""; dateInput.value = "";
});

// 12) Fun Couple Quiz
const quizQ = $("#quizQ"), quizA = $("#quizA"), quizList = $("#quizList");
$("#addQuiz")?.addEventListener("click", () => {
  const q = (quizQ.value || "").trim();
  const a = (quizA.value || "").trim();
  if (!q || !a) return;
  const li = document.createElement("li");
  li.textContent = q + " → " + a;
  const x = document.createElement("button"); x.textContent = "✕";
  x.addEventListener("click", ()=> li.remove());
  li.append(x);
  quizList.append(li);
  quizQ.value = ""; quizA.value = "";
});

  // Quotes
  const quotes = [
    "You are my today and all of my tomorrows.",
    "Love is composed of a single soul inhabiting two bodies.",
    "Every love story is beautiful, but ours is my favorite.",
    "In your smile, I see something more beautiful than the stars."
  ];
  const loveQuote = document.getElementById("loveQuote");
  loveQuote.textContent = quotes[Math.floor(Math.random() * quotes.length)];

  // Mood Tracker
  const moods = document.querySelectorAll("#moods button");
  const savedMood = document.getElementById("savedMood");
  let currentMood = localStorage.getItem("mood");
  if (currentMood) savedMood.textContent = currentMood;

  moods.forEach(b => {
    b.addEventListener("click", () => {
      localStorage.setItem("mood", b.textContent);
      savedMood.textContent = b.textContent;
    });
  });

  // Gratitude Note
  const gratitude = document.getElementById("gratitude");
  const saveGratitude = document.getElementById("saveGratitude");
  const lastGratitude = document.getElementById("lastGratitude");

  let storedGratitude = localStorage.getItem("gratitude");
  if (storedGratitude) lastGratitude.textContent = storedGratitude;

  saveGratitude.addEventListener("click", () => {
    if (gratitude.value.trim() !== "") {
      localStorage.setItem("gratitude", gratitude.value);
      lastGratitude.textContent = gratitude.value;
      gratitude.value = "";
    }
  });

  // ========== Memory Vault ==========
document.getElementById("saveMemory").addEventListener("click", function () {
  const memory = document.getElementById("memoryText").value.trim();
  if (memory) {
    localStorage.setItem("memoryVault", memory);
    document.getElementById("lastMemory").textContent = memory;
    document.getElementById("memoryText").value = "";
  }
});

// Load saved memory on refresh
window.addEventListener("load", function () {
  const savedMemory = localStorage.getItem("memoryVault");
  if (savedMemory) {
    document.getElementById("lastMemory").textContent = savedMemory;
  }
});

// ========== Daily Challenge ==========
const challenges = [
  "Write a love letter 💌",
  "Plan a surprise date 🌹",
  "Cook dinner together 🍲",
  "Watch your first movie again 🎬",
  "Take a selfie and save in album 📸",
  "Say 3 things you love about each other 💕",
];

function loadChallenge() {
  const random = challenges[Math.floor(Math.random() * challenges.length)];
  document.getElementById("dailyChallenge").textContent = random;
}

// Load one challenge initially
window.addEventListener("load", loadChallenge);

// Change challenge on button click
document.getElementById("newChallenge").addEventListener("click", loadChallenge);
