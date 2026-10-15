# 霜璃 · 侧脸形状修复

用户反馈：跟随鼠标左右转头和左右移动时，脸型都显得奇怪。检查发现旧侧脸的面颊与下颌偏平、偏长，鼻口和下巴向前突出，与正脸的短圆比例不一致。

本轮沿用现有正脸与角色身份，修复两组移动和两组视线，共 32 帧。其余七组状态的 41 帧保持原有像素。新侧脸使用较浅的四分之三转头，保留双眼和远眼的透视缩短、细小鼻尖、圆润脸颊、短下巴；头颈与眼睛协调转动。

所有视觉重绘使用内置 imagegen，完整源行经过 Pets 技能附带工具提取和验证；没有手工绘制、脸部变形或单格拼补。生成提示、引用哈希、候选和实际报告保存在 `run/`。云端 Library 接口不可用，本地版本目录保留完整资料。

## 查看与回退

- [本轮开始时下载的宠物](inputs/current-spritesheet.png)
- [旧版侧脸问题检查图](inputs/native-diagnosis.png)
- [转头与移动交互对比](experience-preview.html)
- [最终精灵图](run/final/spritesheet-extended.png)
- [脸型前后对比](run/previews/comparisons/face-shape-before-after.png)
- [连续转头对比](run/previews/comparisons/look-faces-before-after.gif)
- [向右移动对比](run/previews/comparisons/running-right-before-after.gif)
- [向左移动对比](run/previews/comparisons/running-left-before-after.gif)
- [全部动作](run/previews/all-states.gif) / [MP4](run/previews/all-states.mp4)
- [视线循环](run/previews/look-loop.gif)

最终成品已通过全部验收并更新原有「霜璃」。`repair-plan.json` 和实际 `run/qa/` 报告记录最终状态。

## 完成验证

最终 PNG 3,538,414 字节，SHA-256：`4608b7258cfd489db3d07e64128da9df03f4f852bf2d31121babc3a8bd9a9696`。

- 32 帧重绘，41 帧保留像素验证通过。
- 结构、透明格、边缘去色、组件提取及最终帧检查通过。
- 十六方向语义、三人独立盲检、独立最终视觉复核及综合质量检查通过。
- 正常大小、75% 小尺寸与深色背景的对比检查通过；GIF 和 MP4 从最终编码图导出。
- Pets 预检通过，原有宠物 ID、名称、描述和活动选择保持不变。
- 重新下载保存版本，与本地最终图像解码后的 RGBA 逐像素相同。

部分斜向姿势相近，作为已复核提示保留。扫描器标记的翼下和裙边外侧空隙经过深色背景独立检查，确认为角色外部留白，没有穿过身体的透明裂缝。157.5→180 的像素差异统计提示也经过完整循环复核。详见 `run/qa/independent-final-review.json`、`pet-quality.json`、`blind-validation.json` 和 `stored-verification.json`。

有效生成提示保存在 `run/prompts/`；内置 imagegen 为本轮全部视觉重绘来源。`assemble_and_check.py` 仅调用技能附带的实际合成与检查工具，`export_face_comparisons.py` 仅裁切成品像素用于对比，均不会自行绘制脸部。
