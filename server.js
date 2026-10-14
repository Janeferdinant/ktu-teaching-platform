/**
 * Academic Teaching Platform - Dev & Preview Server
 * Jane Rose | Asst. Professor | CSE
 */

const http = require('http');
const fs = require('fs');
const path = require('path');

const PORT = process.env.PORT || 5173;
const BASE_DIR = __dirname;

const MIME_TYPES = {
  '.html': 'text/html; charset=utf-8',
  '.css': 'text/css; charset=utf-8',
  '.js': 'application/javascript; charset=utf-8',
  '.json': 'application/json; charset=utf-8',
  '.svg': 'image/svg+xml',
  '.pdf': 'application/pdf',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.ico': 'image/x-icon'
};

const server = http.createServer((req, res) => {
  let reqPath = decodeURI(req.url.split('?')[0]);

  // Root redirect to faculty dashboard
  if (reqPath === '/' || reqPath === '') {
    res.writeHead(302, { 'Location': '/faculty-dashboard/' });
    return res.end();
  }

  // Canonical dashboard rewrite
  if (reqPath === '/faculty-dashboard' || reqPath === '/faculty-dashboard/') {
    reqPath = '/faculty-dashboard/index.html';
  }

  // Trailing slash redirect for course routes: /courses/:code -> /courses/:code/
  const noSlashCourse = reqPath.match(/^\/courses\/([A-Za-z0-9_-]+)$/);
  if (noSlashCourse && noSlashCourse[1] !== 'slides') {
    res.writeHead(301, { 'Location': `/courses/${noSlashCourse[1]}/` });
    return res.end();
  }

  // Trailing slash redirect for slides routes: /courses/:code/slides -> /courses/:code/slides/
  const noSlashSlides = reqPath.match(/^\/courses\/([A-Za-z0-9_-]+)\/slides$/);
  if (noSlashSlides) {
    res.writeHead(301, { 'Location': `/courses/${noSlashSlides[1]}/slides/` });
    return res.end();
  }

  // Legacy/accidental relative slide requests: /courses/slides/lecture_slides.html
  if (reqPath === '/courses/slides/lecture_slides.html' || reqPath === '/slides/lecture_slides.html') {
    const referer = req.headers['referer'] || '';
    const refMatch = referer.match(/\/courses\/([A-Za-z0-9_-]+)/);
    const targetCode = (refMatch && refMatch[1] !== 'slides') ? refMatch[1] : 'PCCST303';
    reqPath = `/courses/${targetCode}/slides/lecture_slides.html`;
  }

  // Legacy/accidental relative teaching plan requests
  if (reqPath === '/courses/teaching-plan/teaching_plan_46h.json' || reqPath === '/teaching-plan/teaching_plan_46h.json') {
    const referer = req.headers['referer'] || '';
    const refMatch = referer.match(/\/courses\/([A-Za-z0-9_-]+)/);
    const targetCode = (refMatch && refMatch[1] !== 'slides') ? refMatch[1] : 'PCCST303';
    reqPath = `/courses/${targetCode}/teaching-plan/teaching_plan_46h.json`;
  }

  // Dynamic route for direct slides: /courses/:code/slides/ or /courses/:code/slides/lecture_slides.html
  const slidesMatch = reqPath.match(/^\/courses\/([A-Za-z0-9_-]+)\/slides\/?(?:lecture_slides\.html)?$/);
  if (slidesMatch && slidesMatch[1] !== 'slides') {
    const code = slidesMatch[1];
    reqPath = `/courses/${code}/slides/lecture_slides.html`;
  }

  // Dynamic route for course home: /courses/:code/ -> /courses/:code/website/index.html
  const courseMatch = reqPath.match(/^\/courses\/([A-Za-z0-9_-]+)\/$/);
  if (courseMatch && courseMatch[1] !== 'slides') {
    const code = courseMatch[1];
    reqPath = `/courses/${code}/website/index.html`;
  }

  // Map legacy /PCCST303/website/* -> /courses/PCCST303/website/*
  if (reqPath.startsWith('/PCCST303/website/')) {
    reqPath = '/courses' + reqPath;
  }

  // Map to local file system
  let filePath = path.join(BASE_DIR, reqPath);

  // If path is directory, look for index.html
  if (fs.existsSync(filePath) && fs.statSync(filePath).isDirectory()) {
    filePath = path.join(filePath, 'index.html');
  }

  if (!fs.existsSync(filePath)) {
    res.writeHead(404, { 'Content-Type': 'text/html; charset=utf-8' });
    res.end(`<h1>404 Not Found</h1><p>The requested file <code>${reqPath}</code> was not found on this server.</p><hr><p>Jane Rose | Asst. Professor | CSE</p>`);
    return;
  }

  const ext = path.extname(filePath).toLowerCase();
  const contentType = MIME_TYPES[ext] || 'application/octet-stream';

  fs.readFile(filePath, (err, data) => {
    if (err) {
      res.writeHead(500, { 'Content-Type': 'text/plain' });
      res.end('500 Internal Server Error');
      return;
    }
    res.writeHead(200, {
      'Content-Type': contentType,
      'Access-Control-Allow-Origin': '*'
    });
    res.end(data);
  });
});

server.listen(PORT, () => {
  console.log(`===================================================================`);
  console.log(`Academic Teaching Platform - Jane Rose, Asst. Professor, CSE`);
  console.log(`Server running at: http://localhost:${PORT}`);
  console.log(`Faculty Dashboard: http://localhost:${PORT}/faculty-dashboard/`);
  console.log(`Pilot Course Site: http://localhost:${PORT}/courses/PCCST303/`);
  console.log(`Presentation Deck: http://localhost:${PORT}/courses/PCCST303/slides/`);
  console.log(`===================================================================`);
});
