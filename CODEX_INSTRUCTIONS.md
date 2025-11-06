# CODEX: Start Fresh - New Task

## 🔴 STOP - Ignore Previous Context

You are NOT continuing achievement work. That was a different branch and different task.

## ✅ Your New Task: Post-Story Emotional Check

**Branch:** `codex-post-story-check`
**Task File:** `CODEX_WEEK1_TASK_B.md`

### What You Need to Do:

1. **Read the task file:**
   ```bash
   cat CODEX_WEEK1_TASK_B.md
   ```

2. **This is a NEW feature from scratch:**
   - Create `lib/post_story_feelings_dialog.dart` (NEW FILE)
   - Modify `lib/models.dart` to add pre/post emotion fields
   - Modify `lib/story_result_screen.dart` to show post-story check
   - Modify `lib/main_story.dart` to pass pre-feeling data

3. **Files that DO exist and you CAN use:**
   - `lib/emotions_learning_system.dart` - Read emotion data from here
   - `lib/pre_story_feelings_dialog.dart` - Use as reference for UI patterns
   - `lib/models.dart` - Modify SavedStory model here
   - `lib/story_result_screen.dart` - Show post-check dialog here
   - `lib/main_story.dart` - Pass pre-feeling to result screen

4. **Files that DON'T exist (ignore them):**
   - ❌ achievement_celebration_dialog.dart - NOT on this branch, IGNORE
   - ❌ achievements_screen.dart - NOT on this branch, IGNORE
   - ❌ achievement_service.dart - NOT on this branch, IGNORE

   These files exist on `codex-dev` branch, but you're on `codex-post-story-check`. This is intentional.

### Why Are Achievement Files Missing?

Because you're on a different branch! Achievement work is on `codex-dev`. You are on `codex-post-story-check` for a NEW task.

### Start Here:

```bash
# 1. Confirm you're on the right branch
git branch --show-current
# Should output: codex-post-story-check

# 2. Read the full task
cat CODEX_WEEK1_TASK_B.md

# 3. Check what files exist
ls lib/emotions_learning_system.dart
ls lib/pre_story_feelings_dialog.dart
ls lib/models.dart
ls lib/story_result_screen.dart

# 4. Start implementation following CODEX_WEEK1_TASK_B.md
```

### Your Goal:

Build a post-story emotional check that shows emotion improvement:
- Dialog appears 5 seconds after story completes
- Shows: "Worried went from 4 → 2 ⬇️"
- User can select new emotion and intensity
- Data saved to SavedStory model
- Skippable with "Not now" button

### Key Point:

**This is NOT about achievements. This is about emotion tracking before and after stories.**

Read `CODEX_WEEK1_TASK_B.md` - it has everything you need.

---

## 🚀 Quick Start Checklist

- [ ] Read CODEX_WEEK1_TASK_B.md completely
- [ ] Understand you're building POST-story emotion check
- [ ] Create post_story_feelings_dialog.dart (clone pre_story_feelings_dialog.dart)
- [ ] Add preStoryFeeling and postStoryFeeling fields to SavedStory
- [ ] Show dialog in story_result_screen.dart after 5 seconds
- [ ] Calculate and display emotion delta (before vs after)
- [ ] Test with real stories

**Ignore everything about achievements. Focus only on CODEX_WEEK1_TASK_B.md.**
