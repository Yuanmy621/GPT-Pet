# 霜璃

当前成品为小尺寸体验优化版，已通过现有 Pets 插件更新，保留原宠物 ID 和活动选择。

## 成品与对比

- [透明 v2 精灵图](final/spritesheet-extended.png)：1536×2288，九组动作、十六方向，共 73 帧。
- [全部动作 GIF](previews/all-states.gif) / [MP4](previews/all-states.mp4)
- [工作前后对比](previews/comparisons/running-before-after.gif) / [待机前后对比](previews/comparisons/idle-before-after.gif)
- [实际尺寸交互对比](revisions/small-native-v3/experience-preview.html)
- [视线循环](previews/look-loop.gif) / [跳跃衔接](previews/idle-jump-idle.gif)

## 本轮变化

重绘九组标准动作的 57 帧，加强眼睛与紫灰轮廓，整理发丝与衣裙细节。待机以睁眼和小幅眼睑变化为主；工作保留托腮，等待打开双手，检查结果向下侧视并点头。左右移动分别生成，跳跃保留角色头部大小，通过屈膝与收腿表达离地。

新视线候选在独立复核中出现转头和比例跳变，均未上传。最终保留原有通过检查的十六方向，其成品像素与本轮开始时下载的宠物完全一致。最终标准动作与保留视线之间的比例和身份衔接已通过独立复核。

当前源图、有效提示、被否决候选及实际报告见 [本轮完整记录](revisions/small-native-v3/README.md)。根部 decoded、frames、prompts 与原有作业记录保留早期制作过程。

## 验证

最终 PNG 3,567,404 字节，SHA-256：`23b61ab26a31258c9b9a4b0a1c59e0eef8cd20dbbc2ad5b2ba513cc8861fe97b`。

结构和透明格、边缘去色、标准帧、方向语义、三位独立盲检、综合质量以及 Pets 预检均通过。最终跳跃可见边界峰值离地 40 px，落地基线差 0 px。保留视线在 157.5→180 处仍有一个像素差异统计提示，已通过原生尺寸视觉复核。

[保存验证](qa/stored-verification.json)确认服务保存的图像与本地成品解码像素一致；PNG 编码字节可因服务重新编码而不同。旧版本保存在 revisions/clarity-motion-v2，本轮开始时下载的精灵图在 revisions/small-native-v3/inputs/current-spritesheet.png，可用于回退。

Pets 每格固定为 192×208。素材接口不提供客户端帧率、插值、点击任务、专注模式或停靠逻辑。实际尺寸对比页只用于素材检查。

历史：[上轮待机与工作修订](revisions/clarity-motion-v2/README.md)。上轮的画面差异指标不代表本轮的客户端帧率。
