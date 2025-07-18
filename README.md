# 🌸 Beauty of Garden

> A visual and interactive web app that finds the most beautiful subarray in a garden using Kadane's Algorithm.

---

## 🧠 Problem Statement

In a long linear garden, each flower has a "beauty" value — some positive (beautiful), some negative (withered or unpleasant).  
The task is to **find the most beautiful continuous group of flowers** that collectively have the highest beauty score.

---

## 🎯 Objective

To develop a frontend web application where users can:
- Input or generate flower beauty values
- Find the subarray of flowers with maximum total beauty
- Visually understand which flowers contribute to the highest beauty

---

## 🔍 Solution Approach

We used **Kadane's Algorithm** to find the **maximum sum subarray** efficiently in linear time.

### 🧮 Kadane's Algorithm (TL;DR):
- Traverse the beauty values one by one
- Maintain a running total of current beauty
- Reset the total if it becomes negative
- Keep updating the best subarray seen so far

---

## 🚀 Features

- ✅ User input for custom beauty scores
- 🎲 Random generator for quick testing
- 📊 Visualization using bar charts (highlighted subarray)
- 🧠 Optimized using Kadane's Algorithm (O(n) time)
- 🌐 Built with **Streamlit** for fast frontend UI

---

## 🛠️ Tech Stack

| Layer        | Tech Used          |
|--------------|--------------------|
| 💻 Frontend  | Streamlit (Python) |
| 🧠 Logic     | Python, Kadane's Algorithm |
| 📊 Visualization | Matplotlib |
| 🎨 UI/UX     | Streamlit Widgets, HTML elements |

---

## 📁 Project Structure

```
📦 BEAUTY_OF_GARDEN
├── app.py                # Main Streamlit App
├── requirements.txt      # Dependencies
├── README.md             # Project Overview
└── assets/               # Images, recordings (optional)
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/beauty-of-garden.git
cd beauty-of-garden
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
streamlit run app.py
```

4. Open your browser and navigate to `http://localhost:8501`

---

## 📈 Output Example

**Input:** `[4, -2, 5, -1, 2, -3, 4]`

**Output:** 
- Most beautiful segment: `[4, -2, 5, -1, 2]` 
- Maximum Beauty Score: `8`
- Bar Chart: Green bars = selected flowers 🌼

---

## 🎨 Algorithm Explanation

**Kadane's Algorithm** works by:

1. Initialize `max_sum = arr[0]` and `current_sum = arr[0]`
2. For each element from index 1 to n-1:
   - `current_sum = max(arr[i], current_sum + arr[i])`
   - `max_sum = max(max_sum, current_sum)`
3. Return `max_sum`

**Time Complexity:** O(n)  
**Space Complexity:** O(1)

---

## 💡 Future Scope

- 🌐 Extend to 2D gardens (grids)
- 📸 Integrate image analysis to auto-assign beauty scores using AI
- 🎨 Improve UI with animations or real flower icons
- 📱 Make it mobile responsive using Streamlit components
- 🔄 Add support for multiple algorithms comparison

---

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 👤 Author

**Reya Garg**  
B.Tech CSE Student | Tech + Design Enthusiast

- 📧 Email: [your.email@example.com]
- 💼 LinkedIn: [linkedin.com/in/yourprofile]
- 🐙 GitHub: [github.com/yourusername]

---

## 📜 License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- Thanks to the creators of Kadane's Algorithm for this elegant solution
- Streamlit community for excellent documentation
- All contributors and testers

---

<div align="center">
  <strong>⭐ Star this repo if you found it helpful! ⭐</strong>
</div>
