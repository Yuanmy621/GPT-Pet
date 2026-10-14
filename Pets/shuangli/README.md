# 霜璃

## 成品

- `final/spritesheet-extended.png`：1536×2288 透明 v2 精灵图，九组标准动画与十六方向视线，共 73 帧。
- `previews/all-states.gif`、`previews/all-states.mp4`：全部动作预览。
- `previews/look-loop.gif`：十六方向视线循环。
- `previews/idle-jump-idle.gif`：待机、跳跃、落地衔接。
- `qa/contact-sheet-final.png`、`qa/direction-sheet.png`：全部帧及方向检查图。

## 生成提示

原始提示集合在 `prompts/`，输入引用与作业状态在 `imagegen-jobs.json`。使用 `references/identity-board.png` 合并三张原始参考的完整画面，以满足单次图像生成输入数量限制；它没有改变参考中的角色设计。各动作修订提示保存在对应 `qa/rows/` 中。

视线生成补充约束：下半身、裙摆、脚、翼与尾保持前向锚定，头颈与原始紫瞳协调转向。第一半圈顺序为向上、三个右上、向右、三个右下；第二半圈为向下、三个左下、向左、三个左上。每组采用统一比例、落点与独立间距。向右转头时，解剖左侧发饰藏到远侧；向左转头时发饰保留在近侧的屏幕右边。

保留已否决版本以便追溯：初版右移动发饰侧别错误，初版等待比例偏细长，初版沮丧过深蹲下，首个左视线锚朝向错误，首版视线行间距与右下朝向错误，第二版视线行发饰翻侧。均通过 imagegen 修复受影响完整源行，并重新执行对应提取与检查。

## 验证

最终 PNG 3,505,211 字节，SHA-256：`6daae254b0eae8e7ddff1c194970d170e99fa529de8b7e75383095e2a45205ee`。

`final/validation-extended.json`、`qa/pet-quality.json`、`qa/blind-validation.json`、`qa/pets-preflight.json` 均通过。三位独立盲检评审确认所有左右和上下方向。方向连续性在 157.5→180 边界有一个像素差异统计提示，已通过正常尺寸复核：下半身锚定、方向衔接和发饰自然显露均正确。跳跃峰值离地 27 px，落点与待机相同。

全部动画从最终已验证的编码精灵图导出。上传与创建后再次确认文件字节没有变化，稳定宠物元数据保存在 `pet-record.json`，不保存短期上传会话或下载链接。
