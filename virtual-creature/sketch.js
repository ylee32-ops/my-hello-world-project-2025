let charizard;
let fireballs = [];
let sprite;
let bg; // 背景圖

function preload() {
  // 先載入背景與角色圖片
  bg = loadImage('pokemon-1.png');
  sprite = loadImage('pokemon.png');
}

function setup() {
  createCanvas(600, 400);
  imageMode(CENTER);
  charizard = new Creature(width / 2, height / 2 + 50, sprite);
}

function draw() {
  // 🏞️ 顯示背景圖（鋪滿畫布）
  image(bg, width / 2, height / 2, width, height);

  // 顯示角色與火焰
  charizard.update();
  charizard.display();

  // 顯示火焰粒子
  for (let i = fireballs.length - 1; i >= 0; i--) {
    fireballs[i].update();
    fireballs[i].display();
    if (fireballs[i].alpha <= 0) {
      fireballs.splice(i, 1);
    }
  }

  // 能量條
  noStroke();
  fill(255, 80, 0);
  rect(20, 20, charizard.energy * 2, 10);
  fill(255);
  textSize(12);
  text("Energy: " + nf(charizard.energy, 1, 0), 20, 45);
}

function mousePressed() {
  charizard.breatheFire();
}

// ------------------ CLASS Creature ------------------
class Creature {
  constructor(x, y, img) {
    this.x = x;
    this.y = y;
    this.img = img;
    this.energy = 100;
    this.firePower = 12;
  }

  update() {
    this.energy = constrain(this.energy - 0.016, 0, 100);
  }

  display() {
    image(this.img, this.x, this.y, 160, 160);
  }

  breatheFire() {
    if (this.energy > 3) {
      for (let i = 0; i < this.firePower; i++) {
        fireballs.push(new Fire(
          this.x - 70 + random(-5, 5),  // 👈 更靠左邊的噴火點
          this.y - 20 + random(-5, 5),
          random(8, 20),
          random(-8, -3),
          random(-1.5, 1.5)
        ));
      }
      this.energy -= 3;
    }
  }
}

// ------------------ CLASS Fire ------------------
class Fire {
  constructor(x, y, size, vx, vy) {
    this.x = x;
    this.y = y;
    this.size = size;
    this.vx = vx;
    this.vy = vy;
    this.alpha = 255;
  }

  update() {
    this.x += this.vx;
    this.y += this.vy;
    this.alpha -= 5;
  }

  display() {
    noStroke();
    fill(random(200, 255), random(80, 150), 0, this.alpha);
    ellipse(this.x, this.y, this.size);
  }
}

