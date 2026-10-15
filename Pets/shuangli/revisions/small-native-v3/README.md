# 小尺寸体验优化

本轮按「小尺寸形象 → 动作连贯性 → 状态可辨认性」推进，限定在现有 Pets 插件能力内。

## 形象

使用同一张新基础形象重新制作九组标准动作的 57 帧，保留银白长发、紫瞳、双龙角、尖耳、淡紫薄翼、蓬松龙尾、白紫礼裙与银色花结。重点增强眼睛和紫灰轮廓，减少细碎纹样与发丝噪声，让正常显示大小下的表情更容易辨认。十六方向沿用原有通过检查的 16 帧，已逐像素验证与本轮开始时下载的宠物相同。

新视觉由内置 imagegen 根据原始三张角色参考和下载的现有精灵图生成；提取、登记、合成和验证使用 Pets 技能附带工具。

本轮也生成过新的视线候选，但独立复核发现转头与身体宽度的跳变，因此没有上传。`run/candidates/rejected-loop-v1` 至 `rejected-loop-v3` 保存了实际否决结果。最终保留已经通过检查的视线，避免这次标准动作优化引入新的视线问题。旧视线从上版未做边缘清理的完整源图取出，与新标准动作合成后只进行一次最终去色；成品视线像素仍与现有版本完全一致。

## 动作与状态

- 待机：以睁眼和轻微呼吸、眼睑变化为主，减少反复完整闭眼带来的机械感。
- 工作：保持托腮思考，通过小幅连续变化表达专注。
- 等待：双手向上打开，配合期待的眼神和轻微歪头。
- 检查结果：手在腰前，向下侧视、轻点头后回正。
- 移动：左右分别生成，保留交替步态及发饰正确侧别。
- 跳跃：通过屈膝、收腿和裙摆变化保留头部大小及落地基线。
- 失落：温和的短暂反应后恢复平静。

## 对比与文件

- [实际尺寸交互对比](experience-preview.html)：切换动作、尺寸、底色，暂停并逐帧查看。
- [原有精灵图](inputs/current-spritesheet.png)：本轮开始时下载的版本，可用于回退。
- [新基础形象原生尺寸对比](run/qa/base-native-comparison.png)
- [待机前后对比](run/previews/comparisons/idle-before-after.gif) / [工作前后对比](run/previews/comparisons/running-before-after.gif)
- [原生尺寸、三种底色检查](run/previews/comparisons/native-backgrounds.png)
- [标准动作逐帧图](run/qa/contact-standard.png)
- [最终透明精灵图](run/final/spritesheet-extended.png)
- [全部动作 GIF](run/previews/all-states.gif) / [MP4](run/previews/all-states.mp4)
- [待机、跳跃、待机衔接](run/previews/idle-jump-idle.gif)
- [方向检查图](run/qa/direction-sheet.png) / [视线循环](run/previews/look-loop.gif)

每个源动作的提示词、被否决版本和实际检查结果保存在 `run/qa/rows/`；共用输入和基础形象在 `run/references/`；生成作业记录在 `run/imagegen-jobs.json`。当前工作资料保存在本地，云端 Library 接口不可用。

## 能力边界

Pets 使用固定的九组动作和十六方向，每格为 192×208 像素。本轮可以改进画面和动作语义，不能通过素材设置更高的客户端帧率、更长的随机眨眼间隔、点击任务入口、专注模式或停靠逻辑。交互对比页只用于检查素材，其控制项不会改变 Pets 的实际设置。

完整验证结果以 `run/final/validation-extended.json`、`run/qa/pet-quality.json`、`run/qa/blind-validation.json`、`run/qa/pets-preflight.json` 为准；保存后的图像像素核对记录在 `run/qa/stored-verification.json`。

## 已交付验证

最终 PNG 3,567,404 字节，SHA-256：`23b61ab26a31258c9b9a4b0a1c59e0eef8cd20dbbc2ad5b2ba513cc8861fe97b`。九组动作共 57 帧重绘，十六方向 16 帧保留。结构、透明格、去色、帧检查、方向语义、三位独立盲检、独立视觉复核、综合质量及 Pets 文件预检通过。跳跃可见边界峰值离地 40 px，落地基线差 0 px。

已通过现有 Pets 插件更新原有「霜璃」，宠物 ID、名称、描述和活动选择保持不变。重新下载服务保存的精灵图，与本地最终图像逐像素一致。旧版与所有未上传候选均已保留。保留视线在 157.5→180 的像素差异统计提示经过原生尺寸复核；它来自原有视线。

版本索引：`../../current-version.json`。根部 final、previews 与当前 QA 摘要已同步到本轮成品；本目录的完整来源和实际报告保留不变。
