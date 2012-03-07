function P(x,y) {
	return {x: x, y: y};
}

function J() {
	return Math.floor(Math.random() * 16);
}

function R() {
	do {
		z={x: J(), y: J()}
	} while (T(z))
	return z;
}

function A(a,b) {
	return {x: a.x + b.x, y: a.y + b.y};
}

function Q(a,b) {
	return a.x == b.x && a.y == b.y;
}

function O(p) {
	return p.x < 0 || p.x > 15 || p.y < 0 || p.y > 15;
}

function T(p) {
	return s.filter(Q.bind(this,p)).length;
}

function M(p) {
	if (p.x != -d.x && p.y != -d.y)
		m = p;
}

function B() {
	s.map(function(p) {
		c.fillRect(p.x << 3, p.y << 3, 8, 8);
	});
}

function C() {
	c.beginPath();
	c.arc((a.x << 3) + 4, (a.y << 3) + 4, 4, 0, 7);
	c.fill();
}

function F() {
	c.fillStyle='red';
	B();
	setTimeout(I, 5000);
}

function E() {
	d = m;
	var n = A(s[0],d);
	(O(n) || T(n)) && (F(),1) || setTimeout(E, 350 - s.length * 5);
	s.unshift(n);
	Q(s[0],a) && (a = R()) || s.pop();

	c.clearRect(0,0,128,128);
	B();
	C();
}

window.addEventListener('keydown', function(e) {
	M({ 37: P(-1,0), 38: P(0,-1), 39: P(1,0), 40: P(0,1) }[e.keyCode]);
}, false);

function I() {
	document.body.innerHTML = '<canvas width=128 height=128 style="width:256px;height:256px;border:8px solid black"></canvas>';
	c = document.body.firstChild.getContext('2d');

	s = [P(8,8),P(7,8),P(6,8)];
	a = R();
	m = P(1,0);

	E();
}

setTimeout(I,0);

