# 🐼 ANGrI - An N-Gram Interface

> A delightful way to practice Chinese characters using n-grams! 🎉

## 🌟 Features

- 🔤 Generate Chinese characters using n-gram models (1-4 characters)
- 🗣️ Text-to-speech pronunciation with native Chinese voice
- 📝 English translations for better understanding
- 📚 Review queue to practice previously seen characters
- ⌨️ Keyboard shortcuts for speedy learning

## 🎮 How to Use

1. **Choose Your Level**
   - Pick from 1-gram to 4-gram models (use keys 1-4)
   - More characters = more challenge! 🎯

2. **Practice Controls**
   - ➡️ (Right Arrow) - Generate new characters
   - ⬆️ (Up Arrow) - Hear pronunciation
   - ⬇️ (Down Arrow) - Show/hide translation
   - ⬅️ (Left Arrow) - Add to review queue
   - Q - Switch to review mode

## 🛠️ Technical Details

Built with:
- Flask backend for serving n-gram models
- Web Speech API for pronunciation
- Tailwind CSS for sleek styling
- Custom pickle loader for model management

## 🎨 Interface

The app features a clean, three-panel design:
- Left: Review queue for practice items
- Center: Main display area with pinyin and translations
- Right: N-gram size selection and mode controls

## 🚀 Getting Started

1. Install dependencies:

pip install flask pypinyin

2. Run the Flask server:

python main.py


3. Visit `http://localhost:5000` and start learning! 🎓

## 🎵 Fun Fact

Why "ANGrI"? Because it's "An N-Gram Interface" and sometimes learning Chinese can make you a little angry! 😄 But don't worry, we make it fun! 

## 🤗 Contributing

Feel free to contribute! Whether it's:
- 🐛 Bug fixes
- ✨ New features
- 📚 Better translations
- 🎨 UI improvements

We welcome all contributions with open arms! 

---

Made with ❤️ for Chinese language learners everywhere