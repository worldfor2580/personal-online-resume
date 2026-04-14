import re

# ================== FIX INDEX.HTML ==================
print("Updating index.html...")
with open(r'K:\AI_Test\zip\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Check if already modified
if 'openVideo' in content:
    print("index.html already has video support, skipping")
else:
    # Add videos section
    old = '''        <section id="games">
            <h2 class="section-title">游戏作品集</h2>
            <div class="grid" id="games-grid"></div>
        </section>
    </main>'''
    new = '''        <section id="games">
            <h2 class="section-title">游戏作品集</h2>
            <div class="grid" id="games-grid"></div>
        </section>

        <section id="videos">
            <h2 class="section-title">视频展示</h2>
            <div class="video-grid" id="videos-grid"></div>
        </section>
    </main>'''
    content = content.replace(old, new)

    # Add video modal
    old = '''    <!-- Modal -->
    <div class="modal-overlay" id="game-modal" onclick="closeModal(event)">'''
    new = '''    <!-- Video Modal -->
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
    content = content.replace(old, new)

    # Add video CSS
    old = '''        .card-tags { display: flex; flex-wrap: wrap; gap: 0.5rem; }
        .card-tag '''
    new = '''        .card-tags { display: flex; flex-wrap: wrap; gap: 0.5rem; }
        .card-tag { font-size: 0.75rem; padding: 0.25rem 0.5rem; background: rgba(99, 102, 241, 0.1); color: var(--accent-primary); border-radius: var(--radius-md); font-weight: 500; }

        /* Video Grid */
        .video-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap: 2rem; }
        .video-card { background: var(--bg-card); border: 1px solid var(--border-color); border-radius: var(--radius-lg); overflow: hidden; transition: all 0.3s; cursor: pointer; }
        .video-card:hover { transform: translateY(-4px); box-shadow: var(--shadow-lg); border-color: var(--accent-primary); }
        .video-placeholder { width: 100%; aspect-ratio: 16/9; display: flex; align-items: center; justify-content: center; background: var(--bg-secondary); font-size: 3rem; }
        .video-info { padding: 1rem; }
        .video-title { font-size: 1rem; font-weight: 700; margin-bottom: 0.5rem; color: var(--text-primary); }
        .video-desc { font-size: 0.875rem; color: var(--text-secondary); display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden; }
        .card-tag '''
    content = content.replace(old, new)

    # Add nav item for videos
    old = '''            <li><a href="#games">项目</a></li>
            <li><a href="/personal-online-resume/admin.html">管理</a></li>'''
    new = '''            <li><a href="#videos">视频</a></li>
            <li><a href="#games">项目</a></li>
            <li><a href="/personal-online-resume/admin.html">管理</a></li>'''
    content = content.replace(old, new)

    # Add videos JS
    old = '''            // Games
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
    new_code = '''            // Games
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
    content = content.replace(old, new_code)

    # Add openVideo and closeVideoModal functions
    old = '''        function openGame(index) {
            const game = siteData.games[index];
            if (!game) return;
            
            document.getElementById('modal-title').textContent = game.title;'''
    new_code = '''        function openVideo(index) {
            const video = siteData.videos[index];
            if (!video) return;
            document.getElementById('video-modal-title').textContent = video.title;
            const bvid = video.bvid || (video.url || '').match(/BV[a-zA-Z0-9]+/)?.[0] || '';
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
    content = content.replace(old, new_code)

    # Update ESC handler
    old = '''        document.addEventListener('keydown', e => {
            if (e.key === 'Escape') closeModal(null, true);
        });'''
    new_code = '''        document.addEventListener('keydown', e => {
            if (e.key === 'Escape') {
                closeModal(null, true);
                closeVideoModal(null, true);
            }
        });'''
    content = content.replace(old, new_code)

    with open(r'K:\AI_Test\zip\index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("index.html updated")


# ================== FIX ADMIN.HTML ==================
print("Updating admin.html...")
with open(r'K:\AI_Test\zip\public\admin.html', 'r', encoding='utf-8') as f:
    content = f.read()

if 'panel-videos' in content:
    print("admin.html already has video support, skipping")
else:
    # 1. Add nav item for videos (in 内容管理 section)
    old = '''        <nav class="nav-section">
            <div class="nav-section-title">内容管理</div>
            <div class="nav-item" data-panel="games">
                <span class="nav-icon">🎮</span><span>游戏作品</span>
            </div>
        </nav>'''
    new_code = '''        <nav class="nav-section">
            <div class="nav-section-title">内容管理</div>
            <div class="nav-item" data-panel="videos">
                <span class="nav-icon">🎬</span><span>视频管理</span>
            </div>
            <div class="nav-item" data-panel="games">
                <span class="nav-icon">🎮</span><span>游戏作品</span>
            </div>
        </nav>'''
    content = content.replace(old, new_code)

    # 2. Add videos panel HTML before games panel
    old = '''        <!-- 游戏作品 -->
        <div class="panel" id="panel-games">'''
    new_code = '''        <!-- 视频管理 -->
        <div class="panel" id="panel-videos">
            <div class="page-header">
                <h1 class="page-title">视频管理</h1>
            </div>
            <div class="form-section">
                <div class="form-section-title">添加视频</div>
                <div class="form-grid">
                    <div class="form-group">
                        <label class="form-label">视频标题</label>
                        <input type="text" class="form-input" id="video-title" placeholder="例如：夜郎ARPG实机演示">
                    </div>
                    <div class="form-group">
                        <label class="form-label">B站链接或 BV号</label>
                        <input type="text" class="form-input" id="video-url" placeholder="例如：BV1TJ4y1f7PH 或完整B站视频链接">
                    </div>
                </div>
                <div class="form-group">
                    <label class="form-label">视频描述</label>
                    <textarea class="form-input" id="video-desc" rows="3" placeholder="简要描述视频内容（选填）"></textarea>
                </div>
                <button class="btn btn-primary" onclick="addVideo()">添加视频</button>
            </div>
            <div class="form-section" style="margin-top:1.5rem;">
                <div class="form-section-title">视频列表</div>
                <div class="data-list" id="videos-list"></div>
            </div>
        </div>

        <!-- 游戏作品 -->
        <div class="panel" id="panel-games">'''
    content = content.replace(old, new_code)

    # 3. Add video JS functions before games JS
    old = '''        // ============ Games Management ============'''
    new_code = '''        // ============ Videos Management ============
        function extractBvid(url) {
            const match = (url || '').match(/BV[a-zA-Z0-9]+/);
            return match ? match[0] : (url || '').trim();
        }

        function addVideo() {
            const title = document.getElementById('video-title').value.trim();
            const url = document.getElementById('video-url').value.trim();
            const desc = document.getElementById('video-desc').value.trim();
            if (!title || !url) { alert('请填写标题和链接'); return; }
            const bvid = extractBvid(url);
            siteData.videos = siteData.videos || [];
            siteData.videos.push({ title, bvid, url, description: desc });
            saveToLocalStorage();
            renderVideosList();
            document.getElementById('video-title').value = '';
            document.getElementById('video-url').value = '';
            document.getElementById('video-desc').value = '';
            showToast('视频添加成功');
        }

        function deleteVideo(index) {
            if (!confirm('确定删除该视频？')) return;
            siteData.videos.splice(index, 1);
            saveToLocalStorage();
            renderVideosList();
            showToast('视频已删除');
        }

        function renderVideosList() {
            const list = document.getElementById('videos-list');
            if (!list) return;
            const videos = siteData.videos || [];
            if (videos.length === 0) {
                list.innerHTML = '<div style="padding:1rem;color:var(--text-tertiary)">暂无视频，点击上方添加</div>';
                return;
            }
            list.innerHTML = videos.map((v, i) => `
                <div style="display:flex;justify-content:space-between;align-items:center;padding:1rem;border-bottom:1px solid var(--border-color)">
                    <div>
                        <div style="font-weight:600">${v.title}</div>
                        <div style="font-size:0.8rem;color:var(--text-tertiary);margin-top:0.25rem;">${v.bvid || v.url}</div>
                        ${v.description ? `<div style="font-size:0.85rem;color:var(--text-secondary);margin-top:0.25rem;">${v.description}</div>` : ''}
                    </div>
                    <button onclick="deleteVideo(${i})" style="background:#ef4444;color:#fff;border:none;padding:0.4rem 0.75rem;border-radius:6px;cursor:pointer;font-size:0.85rem">删除</button>
                </div>
            `).join('');
        }

        // ============ Games Management ============'''
    content = content.replace(old, new_code)

    # 4. Add renderVideosList to renderAll
    old = '''        function renderAll() {
            renderProfile();
            renderGames();
            renderResume();
        }'''
    new_code = '''        function renderAll() {
            renderProfile();
            renderVideosList();
            renderGames();
            renderResume();
        }'''
    content = content.replace(old, new_code)

    with open(r'K:\AI_Test\zip\public\admin.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("admin.html updated")

print("Done!")
