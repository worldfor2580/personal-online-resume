with open(r'K:\AI_Test\zip\public\admin.html', 'r', encoding='utf-8') as f:
    content = f.read()

# The video functions to add
video_js = '''
        // ============ Videos Management ============
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
            data.videos = data.videos || [];
            data.videos.push({ title, bvid, url, description: desc });
            saveToLocalStorage();
            renderVideosList();
            document.getElementById('video-title').value = '';
            document.getElementById('video-url').value = '';
            document.getElementById('video-desc').value = '';
            showToast('视频添加成功');
        }

        function deleteVideo(index) {
            if (!confirm('确定删除该视频？')) return;
            data.videos.splice(index, 1);
            saveToLocalStorage();
            renderVideosList();
            showToast('视频已删除');
        }

        function renderVideosList() {
            const list = document.getElementById('videos-list');
            if (!list) return;
            const videos = data.videos || [];
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

'''

# Insert before function renderGames()
target = '        function renderGames() {'
if target in content:
    content = content.replace(target, video_js + target)
    print('Inserted video JS before renderGames')
else:
    print('ERROR: target not found')

with open(r'K:\AI_Test\zip\public\admin.html', 'w', encoding='utf-8') as f:
    f.write(content)
