import re

# ================== FIX INDEX.HTML ==================
with open(r'K:\AI_Test\zip\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add videos section after games section
old_games_section = '''        <section id="games">
            <h2 class="section-title">游戏作品集</h2>
            <div class="grid" id="games-grid"></div>
        </section>
    </main>'''

new_games_section = '''        <section id="games">
            <h2 class="section-title">游戏作品集</h2>
            <div class="grid" id="games-grid"></div>
        </section>

        <section id="videos">
            <h2 class="section-title">视频展示</h2>
            <div class="video-grid" id="videos-grid"></div>
        </section>
    </main>'''

content = content.replace(old_games_section, new_games_section)

# 2. Add video modal HTML before game-modal
old_modal = '''    <!-- Modal -->
    <div class="modal-overlay" id="game-modal" onclick="closeModal(event)">'''

new_modal = '''    <!-- Video Modal -->
    <div class="modal-overlay" id="video-modal" onclick="closeVideoModal(event)">
        <div class="modal">
            <div class="modal-header">
                <h3 class="modal-title" id="video-modal-title"></h3>
                <button class="modal-close" onclick="closeVideoModal(null, true)">&times;</button>
            </div>
            <div class="modal-body" id="video-modal-body"></div>
        </div>
    </div>

    <!-- Game Modal -->
    <div class="modal-overlay" id="game-modal" onclick="closeModal(event)">'''

content = content.replace(old_modal, new_modal)

# 3. Add CSS for video grid and video cards
old_css = '''        .card-desc { color: var(--text-secondary); font-size: 0.95rem; margin-bottom: 1.5rem; flex-grow: 1; display: -webkit-box; -webkit-line-clamp: 3; -webkit-box-orient: vertical; overflow: hidden; }'''

new_css = '''        .card-desc { color: var(--text-secondary); font-size: 0.95rem; margin-bottom: 1.5rem; flex-grow: 1; display: -webkit-box; -webkit-line-clamp: 3; -webkit-box-orient: vertical; overflow: hidden; }

        /* Video Grid */
        .video-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap: 2rem; }
        .video-card { background: var(--bg-card); border: 1px solid var(--border-color); border-radius: var(--radius-lg); overflow: hidden; transition: all 0.3s; cursor: pointer; }
        .video-card:hover { transform: translateY(-4px); box-shadow: var(--shadow-lg); border-color: var(--accent-primary); }
        .video-thumbnail { width: 100%; aspect-ratio: 16/9; background: var(--bg-secondary); position: relative; }
        .video-thumbnail iframe { width: 100%; height: 100%; border: none; }
        .video-info { padding: 1rem; }
        .video-title { font-size: 1rem; font-weight: 700; margin-bottom: 0.5rem; color: var(--text-primary); }
        .video-desc { font-size: 0.875rem; color: var(--text-secondary); display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden; }
        .video-placeholder { width: 100%; aspect-ratio: 16/9; display: flex; align-items: center; justify-content: center; background: var(--bg-secondary); font-size: 3rem; }'''

content = content.replace(old_css, new_css)

# 4. Add videos rendering in JS after games rendering
old_games_js = '''            // Games
            const games = siteData.games || [];
            document.getElementById('games-grid').innerHTML = games.map((game, i) => `
                <div class="card" onclick="openGame(${i})">
                    <div class="card-icon">${game.icon || '🎮'}</div>
                    <h3 class="card-title">${game.title}</h3>
                    <p class="card-desc">${game.description}</p>
                    <div class="card-tags">
                        ${(game.tech || []).map(t => `<span class="card-tag">${t}</span>`).join('')}
                    </div>
                </div>
            `).join('');'''

new_games_js = '''            // Games
            const games = siteData.games || [];
            document.getElementById('games-grid').innerHTML = games.map((game, i) => `
                <div class="card" onclick="openGame(${i})">
                    <div class="card-icon">${game.icon || '🎮'}</div>
                    <h3 class="card-title">${game.title}</h3>
                    <p class="card-desc">${game.description}</p>
                    <div class="card-tags">
                        ${(game.tech || []).map(t => `<span class="card-tag">${t}</span>`).join('')}
                    </div>
                </div>
            `).join('');

            // Videos
            const videos = siteData.videos || [];
            if (videos.length > 0) {
                document.getElementById('videos-grid').innerHTML = videos.map((video, i) => `
                    <div class="video-card" onclick="openVideo(${i})">
                        <div class="video-placeholder">🎬</div>
                        <div class="video-info">
                            <h3 class="video-title">${video.title}</h3>
                            <p class="video-desc">${video.description || ''}</p>
                        </div>
                    </div>
                `).join('');
            } else {
                document.getElementById('videos-grid').innerHTML = '<p style="color: var(--text-tertiary); text-align: center; grid-column: 1/-1;">暂无视频</p>';
            }'''

content = content.replace(old_games_js, new_games_js)

# 5. Add openVideo and closeVideoModal functions after openGame
old_open_game = '''        function openGame(index) {
            const game = siteData.games[index];
            if (!game) return;
            
            document.getElementById('modal-title').textContent = game.title;'''

new_open_game = '''        function openVideo(index) {
            const video = siteData.videos[index];
            if (!video) return;
            document.getElementById('video-modal-title').textContent = video.title;
            const bvid = video.bvid || video.url?.match(/BV[a-zA-Z0-9]+/)?.[0] || '';
            const embedUrl = bvid ? `https://player.bilibili.com/player.html?bvid=${bvid}&page=1` : '';
            let html = '';
            if (embedUrl) {
                html += `<iframe src="${embedUrl}" allowfullscreen style="width:100%;aspect-ratio:16/9;border:none;border-radius:var(--radius-md);margin-bottom:1rem;"></iframe>`;
            }
            if (video.description) {
                html += `<p style="color:var(--text-secondary);white-space:pre-line;">${video.description}</p>`;
            }
            document.getElementById('video-modal-body').innerHTML = html;
            document.getElementById('video-modal').classList.add('active');
            document.body.style.overflow = 'hidden';
        }

        function closeVideoModal(e, force = false) {
            if (force || !e || e.target.id === 'video-modal') {
                document.getElementById('video-modal').classList.remove('active');
                document.body.style.overflow = '';
            }
        }

        function openGame(index) {
            const game = siteData.games[index];
            if (!game) return;
            
            document.getElementById('modal-title').textContent = game.title;'''

content = content.replace(old_open_game, new_open_game)

# 6. Update nav links to include videos
old_nav = '''            <li><a href="#games">项目</a></li>
            <li><a href="/personal-online-resume/admin.html">管理</a></li>'''

new_nav = '''            <li><a href="#videos">视频</a></li>
            <li><a href="#games">项目</a></li>
            <li><a href="/personal-online-resume/admin.html">管理</a></li>'''

content = content.replace(old_nav, new_nav)

# 7. Update ESC key handler
old_esc = '''        document.addEventListener('keydown', e => {
            if (e.key === 'Escape') closeModal(null, true);
        });'''

new_esc = '''        document.addEventListener('keydown', e => {
            if (e.key === 'Escape') {
                closeModal(null, true);
                closeVideoModal(null, true);
            }
        });'''

content = content.replace(old_esc, new_esc)

with open(r'K:\AI_Test\zip\index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('index.html updated')


# ================== FIX ADMIN.HTML ==================
with open(r'K:\AI_Test\zip\public\admin.html', 'r', encoding='utf-8') as f:
    admin_content = f.read()

# 1. Add video section to sidebar
old_sidebar = '''        <div class="nav-item" onclick="showSection('games')">
            <span class="nav-icon">🎮</span>
            <span class="nav-text">游戏管理</span>
        </div>
        <div class="nav-item" onclick="loadData()">
            <span class="nav-icon">💾</span>
            <span class="nav-text">保存数据</span>
        </div>'''

new_sidebar = '''        <div class="nav-item" onclick="showSection('videos')">
            <span class="nav-icon">🎬</span>
            <span class="nav-text">视频管理</span>
        </div>
        <div class="nav-item" onclick="showSection('games')">
            <span class="nav-icon">🎮</span>
            <span class="nav-text">游戏管理</span>
        </div>
        <div class="nav-item" onclick="loadData()">
            <span class="nav-icon">💾</span>
            <span class="nav-text">保存数据</span>
        </div>'''

admin_content = admin_content.replace(old_sidebar, new_sidebar)

# 2. Add video section HTML before games section
old_games_admin = '''    <!-- Games Section -->
    <div class="section" id="games-section" style="display:none">
        <div class="section-header">
            <h2>游戏作品管理</h2>
        </div>
        <div class="card">
            <h3 style="margin-bottom:1rem;">添加游戏</h3>'''

new_games_admin = '''    <!-- Videos Section -->
    <div class="section" id="videos-section" style="display:none">
        <div class="section-header">
            <h2>视频管理</h2>
        </div>
        <div class="card">
            <h3 style="margin-bottom:1rem;">添加视频</h3>
            <div class="form-grid">
                <div class="form-group">
                    <label>视频标题</label>
                    <input type="text" id="video-title" placeholder="例如：夜郎ARPG演示">
                </div>
                <div class="form-group">
                    <label>Bilibili 链接或 BV号</label>
                    <input type="text" id="video-url" placeholder="例如：BV1TJ4y1f7PH 或完整B站链接">
                </div>
            </div>
            <div class="form-group">
                <label>视频描述</label>
                <textarea id="video-desc" rows="3" placeholder="简要描述视频内容"></textarea>
            </div>
            <button class="btn-primary" onclick="addVideo()">添加视频</button>
        </div>
        <div class="card" style="margin-top:1.5rem;">
            <h3 style="margin-bottom:1rem;">视频列表</h3>
            <div id="videos-list"></div>
        </div>
    </div>

    <!-- Games Section -->
    <div class="section" id="games-section" style="display:none">
        <div class="section-header">
            <h2>游戏作品管理</h2>
        </div>
        <div class="card">
            <h3 style="margin-bottom:1rem;">添加游戏</h3>'''

admin_content = admin_content.replace(old_games_admin, new_games_admin)

# 3. Add JS functions for video management (before games JS)
old_games_js_admin = '''        // ============ Games Management ============ '''
new_games_js_admin = '''        // ============ Videos Management ============ '''
new_videos_js = '''        function extractBvid(url) {
            const match = url.match(/BV[a-zA-Z0-9]+/);
            return match ? match[0] : url.trim();
        }

        function addVideo() {
            const title = document.getElementById('video-title').value.trim();
            const url = document.getElementById('video-url').value.trim();
            const desc = document.getElementById('video-desc').value.trim();
            if (!title || !url) { alert('请填写标题和链接'); return; }
            const bvid = extractBvid(url);
            siteData.videos = siteData.videos || [];
            siteData.videos.push({ title, bvid, url, description: desc });
            saveData();
            renderVideosList();
            document.getElementById('video-title').value = '';
            document.getElementById('video-url').value = '';
            document.getElementById('video-desc').value = '';
        }

        function deleteVideo(index) {
            if (!confirm('确定删除？')) return;
            siteData.videos.splice(index, 1);
            saveData();
            renderVideosList();
        }

        function renderVideosList() {
            const list = document.getElementById('videos-list');
            const videos = siteData.videos || [];
            if (videos.length === 0) {
                list.innerHTML = '<p style="color:var(--text-tertiary)">暂无视频</p>';
                return;
            }
            list.innerHTML = videos.map((v, i) => `
                <div style="display:flex;justify-content:space-between;align-items:center;padding:0.75rem;border-bottom:1px solid var(--border-color)">
                    <div>
                        <div style="font-weight:600">${v.title}</div>
                        <div style="font-size:0.8rem;color:var(--text-tertiary)">${v.bvid || v.url}</div>
                    </div>
                    <button onclick="deleteVideo(${i})" style="background:#ef4444;color:#fff;border:none;padding:0.3rem 0.75rem;border-radius:6px;cursor:pointer">删除</button>
                </div>
            `).join('');
        }

        // ============ Games Management ============ '''

admin_content = admin_content.replace(old_games_js_admin, new_videos_js)

# 4. Update render function to include videos rendering
old_render_admin = '''            renderGamesList();
        }

        function renderGamesList() {'''

new_render_admin = '''            renderVideosList();
            renderGamesList();
        }

        function renderVideosList() {'''

admin_content = admin_content.replace(old_render_admin, new_render_admin)

with open(r'K:\AI_Test\zip\public\admin.html', 'w', encoding='utf-8') as f:
    f.write(admin_content)
print('admin.html updated')

print('All done!')
