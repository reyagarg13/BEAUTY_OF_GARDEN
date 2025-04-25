import streamlit as st
import pandas as pd
import random
from flower_logic import max_beauty_garden

# Page configuration with custom theme and favicon
st.set_page_config(
    page_title="🌼 Beauty of Garden",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        color: #2e7d32;
    }
    .subheader {
        font-style: italic;
        color: #558b2f;
    }
    .tip-box {
        padding: 10px;
        border-radius: 5px;
        background-color: #f1f8e9;
        border-left: 5px solid #7cb342;
    }
    .stButton>button {
        background-color: #7cb342;
        color: white;
        border: none;
        padding: 10px 24px;
        font-size: 16px;
        border-radius: 4px;
    }
    .stButton>button:hover {
        background-color: #558b2f;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state for input persistence
if 'default_input' not in st.session_state:
    st.session_state.default_input = "1, 2, 3, 1, 2"

# Handle example presets in sidebar
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/628/628324.png", width=100)
    st.title("Garden Beauty Calculator")
    st.markdown("This app helps you find the most beautiful arrangement of flowers in your garden.")
    
    st.markdown("### How it works")
    st.markdown("""
    1. Enter the beauty values of your flowers
    2. The app calculates the maximum beauty possible
    3. View the optimal arrangement and visualization
    """)
    
    st.markdown("### About")
    st.markdown("Created with ❤️ for garden enthusiasts")
    
    # Example presets
    st.markdown("### Try these examples")
    example_sets = {
        "Small garden": "1, 2, 3, 1, 2",
        "Medium garden": "2, 3, -5, 8, 2, -1, 3, 5",
        "Large garden": "4, -3, 5, -2, -1, 2, 6, -2, 1, 5, -3, 2"
    }
    
    selected_example = st.selectbox("Select a preset:", list(example_sets.keys()))
    
    # Use a callback for the Load Example button
    def load_example():
        st.session_state.default_input = example_sets[selected_example]
    
    st.button("Load Example", on_click=load_example)

# Handle random values generation
def generate_random_values():
    random_values = [random.randint(-10, 10) for _ in range(random.randint(5, 15))]
    st.session_state.default_input = ", ".join(map(str, random_values))

# Main content
st.markdown('<h1 class="main-header">🌸 The Beauty of Garden</h1>', unsafe_allow_html=True)
st.markdown('<h3 class="subheader">"Find the most beautiful flower combination"</h3>', unsafe_allow_html=True)
st.markdown("---")

# User input section
col1, col2 = st.columns([3, 1])
with col1:
    user_input = st.text_input(
        "📥 Enter flower beauties (comma-separated):",
        value=st.session_state.default_input
    )
with col2:
    st.markdown("<br>", unsafe_allow_html=True)
    st.button("🎲 Random Values", on_click=generate_random_values)

# Process button and input
if st.button("🌟 Calculate Max Beauty", use_container_width=True):
    try:
        # Clean input and convert to integers
        cleaned_input = user_input.replace(" ", "")
        flowers = [int(x.strip()) for x in cleaned_input.split(",") if x.strip()]
        
        if not flowers:
            st.error("⚠️ Please enter at least one flower beauty value.")
        else:
            result = max_beauty_garden(flowers)
            
            # Results section
            st.markdown("## 📊 Results")
            
            # Display results in columns
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Maximum Beauty", result['max_beauty'])
            with col2:
                st.metric("Starting Position", result.get('start_index', 0) + 1)  # 1-indexed for users
            with col3:
                st.metric("Ending Position", result.get('end_index', 0) + 1)  # 1-indexed for users
            
            # Show the best subarray
            st.markdown("### 🌺 Best Arrangement")
            best_subarray = result['best_subarray']
            
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
                    lambda x: ['background-color: #dcedc8' if x['In Optimal Arrangement'] else '' for i in range(len(x))], 
                    axis=1
                ),
                use_container_width=True
            )
            
            # Visualization section
            st.markdown("### 📈 Flower Beauty Visualization")
            
            # Create tabs for different visualizations
            tab1, tab2 = st.tabs(["Bar Chart", "Line Chart"])
            
            with tab1:
                # Create a color-coded bar chart with conditional formatting
                chart_data = pd.DataFrame({
                    "Position": list(range(1, len(flowers) + 1)),
                    "Beauty": flowers,
                    "Type": ["Selected" if i >= result.get('start_index', 0) and i <= result.get('end_index', 0) 
                             else "Not Selected" for i in range(len(flowers))]
                })
                
                st.bar_chart(chart_data.set_index("Position")["Beauty"], use_container_width=True)
            
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

# Add help section at the bottom
with st.expander("ℹ️ How to use this app"):
    st.markdown("""
    1. Enter the beauty values of your flowers separated by commas
    2. Positive values represent beautiful flowers, negative values represent less appealing plants
    3. Click 'Calculate Max Beauty' to find the optimal arrangement
    4. The app will show you which consecutive flowers give the maximum beauty
    5. Use the 'Random Values' button to generate random beauty values
    6. Try the example presets from the sidebar
    """)