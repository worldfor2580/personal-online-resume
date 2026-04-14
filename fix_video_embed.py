with open(r'K:\AI_Test\zip\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Current video card rendering - shows placeholder, opens modal on click
old_video_render = '''            // Videos
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

# New video card - embed player directly, show title below
new_video_render = '''            // Videos
            const videos = siteData.videos || [];
            if (videos.length > 0) {
                document.getElementById('videos-grid').innerHTML = videos.map((video, i) => {
                    const bvid = video.bvid || (video.url || '').match(/BV[a-zA-Z0-9]+/)?.[0] || '';
                    const embedUrl = bvid ? `https://player.bilibili.com/player.html?bvid=${bvid}&page=1` : '';
                    if (!embedUrl) return '';
                    return `
                        <div class="video-card" style="cursor:default">
                            <iframe src="${embedUrl}" allowfullscreen style="width:100%;aspect-ratio:16/9;border:none;border-radius:var(--radius-md) var(--radius-md) 0 0;"></iframe>
                            <div class="video-info">
                                <h3 class="video-title">${video.title}</h3>
                                ${video.description ? `<p class="video-desc">${video.description}</p>` : ''}
                            </div>
                        </div>
                    `;
                }).join('');
            } else {
                document.getElementById('videos-grid').innerHTML = '<p style="color: var(--text-tertiary); text-align: center; grid-column: 1/-1;">暂无视频</p>';
            }'''

print('Old found:', old_video_render in content)
content = content.replace(old_video_render, new_video_render)
print('New found:', new_video_render in content)

# Remove the onclick that opens modal from video cards (no longer needed)
# Also update video-card CSS to remove hover transform since no modal

with open(r'K:\AI_Test\zip\index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('Done')
