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

  // Dynamic route for any course code: /courses/:courseCode/ -> /courses/:courseCode/website/index.html
  const courseMatch = reqPath.match(/^\/courses\/([A-Za-z0-9_-]+)\/?$/);
  if (courseMatch) {
    const code = courseMatch[1];
    reqPath = `/courses/${code}/website/index.html`;
  }

  // Dynamic route for slides: /courses/:courseCode/slides/? -> /courses/:courseCode/slides/lecture_slides.html
  const slidesMatch = reqPath.match(/^\/courses\/([A-Za-z0-9_-]+)\/slides\/?$/);
  if (slidesMatch) {
    const code = slidesMatch[1];
    reqPath = `/courses/${code}/slides/lecture_slides.html`;
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
