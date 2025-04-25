import streamlit as st
import pandas as pd
import random
import altair as alt
from flower_logic import max_beauty_garden

# Page configuration
st.set_page_config(
    page_title="🌼 Beauty of Garden",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Add Custom CSS for Aesthetic Styling
st.markdown("""
    <style>
        .main {
            background-color: #fef9f4;
            color: #333;
            font-family: 'Comic Sans MS', cursive;
        }
        h1, h2, h3 {
            color: #b24592;
        }
        .stButton button {
            background: linear-gradient(to right, #b24592, #f15f79);
            color: white;
            border: none;
            padding: 10px 20px;
            font-weight: bold;
            border-radius: 12px;
        }
        .tip-box {
            padding: 10px;
            border-radius: 8px;
            background-color: #fff5f7;
            border-left: 5px solid #f15f79;
            margin-bottom: 20px;
        }
        .header-container {
            display: flex;
            justify-content: center;
            align-items: center;
            margin-bottom: 20px;
        }
        .header-emoji {
            font-size: 48px;
            margin-right: 15px;
        }
        .header-title {
            font-size: 36px;
            color: #b24592;
        }
        .custom-subheader {
            text-align: center;
            font-style: italic;
            color: #f15f79;
            margin-bottom: 20px;
        }
        .footer {
            text-align: center;
            color: grey;
            font-size: 14px;
            margin-top: 30px;
            padding-top: 20px;
            border-top: 1px solid #f0f0f0;
        }
        .result-container {
            background-color: #fff;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px;
        }
        .history-item {
            background-color: #fafafa;
            padding: 10px;
            border-radius: 8px;
            margin-bottom: 10px;
            border-left: 3px solid #b24592;
        }
        /* Animation for flower emoji */
        @keyframes flower-bounce {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-10px); }
        }
        .bouncing-flower {
            display: inline-block;
            animation: flower-bounce 2s infinite ease-in-out;
        }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if 'default_input' not in st.session_state:
    st.session_state.default_input = "1, 2, 3, 1, 2"

if 'history' not in st.session_state:
    st.session_state.history = []

if 'dark_mode' not in st.session_state:
    st.session_state.dark_mode = False

# Handle example presets in sidebar
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/628/628324.png", width=100)
    st.title("Garden Beauty Calculator")
    st.markdown("This app helps you find the most beautiful arrangement of flowers in your garden.")
    
    # Toggle dark mode
    def toggle_dark_mode():
        st.session_state.dark_mode = not st.session_state.dark_mode
    
    dark_mode_label = "🌙 Switch to Light Mode" if st.session_state.dark_mode else "🌞 Switch to Dark Mode"
    st.button(dark_mode_label, on_click=toggle_dark_mode)
    
    if st.session_state.dark_mode:
        st.markdown("""
            <style>
                .main {
                    background-color: #1e1e1e;
                    color: #f0f0f0;
                }
                h1, h2, h3 {
                    color: #f15f79;
                }
                .result-container, .history-item {
                    background-color: #2d2d2d;
                    color: #f0f0f0;
                }
                .tip-box {
                    background-color: #2d2d2d;
                }
                .stDataFrame {
                    color: #f0f0f0;
                }
            </style>
        """, unsafe_allow_html=True)
    
    st.markdown("### How it works")
    st.markdown("""
    1. Enter the beauty values of your flowers
    2. The app calculates the maximum beauty possible
    3. View the optimal arrangement and visualization
    """)
    
    # Example presets
    st.markdown("### Try these examples")
    example_sets = {
        "Small garden": "1, 2, 3, 1, 2",
        "Medium garden": "2, 3, -5, 8, 2, -1, 3, 5",
        "Large garden": "4, -3, 5, -2, -1, 2, 6, -2, 1, 5, -3, 2",
        "Rainbow garden": "7, 2, -1, 4, 7, 3, 9, -5, 2, 7"
    }
    
    selected_example = st.selectbox("Select a preset:", list(example_sets.keys()))
    
    # Use a callback for the Load Example button
    def load_example():
        st.session_state.default_input = example_sets[selected_example]
    
    st.button("Load Example", on_click=load_example)
    
    # Clear history button
    def clear_history():
        st.session_state.history = []
    
    st.button("🧹 Clear History", on_click=clear_history)

# Handle random values generation
def generate_random_values():
    random_values = [random.randint(-10, 10) for _ in range(random.randint(5, 15))]
    st.session_state.default_input = ", ".join(map(str, random_values))

# Main header with animation
st.markdown("""
    <div class="header-container">
        <div class="header-emoji bouncing-flower">🌸</div>
        <div class="header-title">The Beauty of Garden</div>
    </div>
""", unsafe_allow_html=True)

st.markdown('<div class="custom-subheader">"Find the most beautiful flower combination"</div>', unsafe_allow_html=True)
st.markdown("---")

# Main layout
col1, col2 = st.columns([3, 1])
with col1:
    user_input = st.text_input(
        "📥 Enter flower beauties (comma-separated):",
        value=st.session_state.default_input
    )
with col2:
    st.markdown("<br>", unsafe_allow_html=True)
    st.button("🎲 Random Garden", on_click=generate_random_values)

# Process button and input
if st.button("🌟 Calculate Max Beauty", use_container_width=True):
    try:
        # Clean input and convert to integers
        cleaned_input = user_input.replace(" ", "")
        flowers = [int(x.strip()) for x in cleaned_input.split(",") if x.strip()]
        
        if not flowers:
            st.error("⚠️ Please enter at least one flower beauty value.")
        else:
            # Easter egg for all negative flowers
            if all(x <= 0 for x in flowers):
                st.info("🌱 Even in the darkest soil, flowers bloom. Keep growing!")
            
            result = max_beauty_garden(flowers)
            
            # Add to history
            st.session_state.history.append({
                'input': user_input,
                'max_beauty': result['max_beauty'],
                'subarray': result['best_subarray']
            })
            
            # Results section in a fancy container
            st.markdown('<div class="result-container">', unsafe_allow_html=True)
            
            st.markdown("## 📊 Results")
            
            # Display results in columns
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Maximum Beauty", result['max_beauty'])
            with col2:
                st.metric("Starting Position", result.get('start_index', 0) + 1)  # 1-indexed for users
            with col3:
                st.metric("Ending Position", result.get('end_index', 0) + 1)  # 1-indexed for users
            
            # Show the best subarray with flower emojis
            st.markdown("### 🌺 Best Arrangement")
            
            # Add flower emojis to output
            flower_emojis = ['🌸', '🌼', '🌺', '🌻', '🌷']
            emoji_subarray = [flower_emojis[i % len(flower_emojis)] + f" `{val}`" for i, val in enumerate(result['best_subarray'])]
            st.markdown("🌹 **Best Subarray with Flowers:** " + " → ".join(emoji_subarray))
            
            # Create a visual representation of the selected vs. unselected flowers
            all_flowers = []
            for i, beauty in enumerate(flowers):
                is_selected = i >= result.get('start_index', 0) and i <= result.get('end_index', 0)
                all_flowers.append({
                    "Position": i+1,  # 1-indexed for users
                    "Beauty Value": beauty,
                    "Selected": "✓" if is_selected else "",
                    "In Optimal Arrangement": is_selected
                })
            
            flower_df = pd.DataFrame(all_flowers)
            
            # Display the data table
            st.dataframe(
                flower_df.style.apply(
                    lambda x: ['background-color: #ffd6e0' if x['In Optimal Arrangement'] else '' for i in range(len(x))], 
                    axis=1
                ),
                use_container_width=True
            )
            
            # Visualization section
            st.markdown("### 📈 Flower Beauty Visualization")
            
            # Create tabs for different visualizations
            tab1, tab2 = st.tabs(["Altair Chart", "Line Chart"])
            
            with tab1:
                # Create Altair chart for prettier visualization
                df = pd.DataFrame({
                    'Index': list(range(1, len(flowers) + 1)),
                    'Beauty': flowers,
                    'Selected': ['Selected' if i >= result.get('start_index', 0) and i <= result.get('end_index', 0) 
                                 else 'Not Selected' for i in range(len(flowers))]
                })
                
                chart = alt.Chart(df).mark_bar().encode(
                    x='Index',
                    y='Beauty',
                    color=alt.Color('Selected', scale=alt.Scale(
                        domain=['Selected', 'Not Selected'],
                        range=['#f15f79', '#d3d3d3']
                    )),
                    tooltip=['Index', 'Beauty', 'Selected']
                ).properties(width=600)
                
                st.altair_chart(chart, use_container_width=True)
            
            with tab2:
                # Line chart showing the running sum (cumulative beauty)
                running_sum = [0]
                for beauty in flowers:
                    running_sum.append(running_sum[-1] + beauty)
                
                running_sum_df = pd.DataFrame({
                    "Position": list(range(len(running_sum))),
                    "Cumulative Beauty": running_sum
                })
                
                st.line_chart(running_sum_df.set_index("Position")["Cumulative Beauty"], use_container_width=True)
            
            st.markdown('</div>', unsafe_allow_html=True)
            
            # Tips box
            st.markdown("""
            <div class="tip-box">
                <h4>💡 Garden Tips</h4>
                <p>Negative beauty values represent plants that might clash with others or require extra maintenance.
                The optimal arrangement balances the positive and negative impacts to maximize overall beauty.</p>
            </div>
            """, unsafe_allow_html=True)

    except ValueError as e:
        st.error("⚠️ Invalid input! Please enter comma-separated integers only.")
    except Exception as e:
        st.error(f"⚠️ An error occurred: {str(e)}")

# Add Results Log (Mini-History)
if st.session_state.history:
    st.markdown("### 🕓 Your Past Results")
    for i, entry in enumerate(reversed(st.session_state.history[-3:]), 1):
        st.markdown(f"""
        <div class="history-item">
            <b>{i}.</b> 💐 Input: {entry['input']} → 
            💎 Max Beauty: {entry['max_beauty']} → 
            🌿 Subarray: {entry['subarray']}
        </div>
        """, unsafe_allow_html=True)

# Add help section at the bottom
with st.expander("ℹ️ How to use this app"):
    st.markdown("""
    1. Enter the beauty values of your flowers separated by commas
    2. Positive values represent beautiful flowers, negative values represent less appealing plants
    3. Click 'Calculate Max Beauty' to find the optimal arrangement
    4. The app will show you which consecutive flowers give the maximum beauty
    5. Use the 'Random Garden' button to generate random beauty values
    6. Try the example presets from the sidebar
    7. Toggle between light and dark mode using the sidebar button
    """)

# Add a Friendly Footer
st.markdown("""
    <div class="footer">
        Made with ❤️ at HackTheGarden. <br>
        Team: CodeBlooms 🌼 | UI by Flower Power Designers
    </div>
""", unsafe_allow_html=True)