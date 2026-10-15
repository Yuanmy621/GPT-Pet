# 霜璃

当前版本已修复左右转头和左右移动时的脸型，并通过现有 Pets 插件更新原有「霜璃」。宠物 ID、名称、描述和活动选择保持不变。

## 成品与对比

- [透明 v2 精灵图](final/spritesheet-extended.png)：1536×2288，73 帧。
- [转头与移动交互对比](revisions/face-shape-v4/experience-preview.html)
- [脸型前后对比](previews/comparisons/face-shape-before-after.png)
- [转头动画对比](previews/comparisons/look-faces-before-after.gif)
- [向右移动对比](previews/comparisons/running-right-before-after.gif) / [向左移动对比](previews/comparisons/running-left-before-after.gif)
- [全部动作 GIF](previews/all-states.gif) / [MP4](previews/all-states.mp4)

## 侧脸修复

旧侧脸的面颊、下颌偏平偏长，鼻口和下巴向前突出。本轮改用双眼可见的四分之三侧脸，以远眼缩窄、头颈转动和短圆下巴表达方向，保留原来的紫瞳、白紫长发、角耳、服装、翼尾和发饰侧别。

重绘两组移动和两组视线，共 32 帧；另外七组状态的 41 帧已确认与本轮开始时下载的宠物逐像素相同。当前源图、提示、候选和检查报告见 [侧脸修复完整记录](revisions/face-shape-v4/README.md)。根部早期 decoded、frames、prompts 和作业记录保留制作历史。

## 验证

最终 PNG 3,538,414 字节，SHA-256：`4608b7258cfd489db3d07e64128da9df03f4f852bf2d31121babc3a8bd9a9696`。

结构、透明格、去色、帧检查、方向语义、三人盲检、独立视觉复核、综合质量及 Pets 预检通过。[保存验证](qa/stored-verification.json)确认服务保存的图像与本地最终图逐像素相同；服务可能重新编码 PNG。

部分斜向角度相近、157.5→180 的像素差异以及翼下/裙边外侧留白扫描均保留为复核提示。独立复核确认没有错误方向、脸型漂移、身体破洞、比例突变或断裂；两组移动步态和转头循环通过。

旧版可从 revisions/face-shape-v4/inputs/current-spritesheet.png 回退。版本索引为 current-version.json。Pets 每格固定为 192×208，本轮没有改变客户端的播放时序或帧率设置。

历史：[小尺寸体验优化](revisions/small-native-v3/README.md) · [上轮待机与工作修订](revisions/clarity-motion-v2/README.md)。
