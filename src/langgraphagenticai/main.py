import streamlit as st
from src.langgraphagenticai.ui.streamlitui.loadui import LoadStreamlitUI
from src.langgraphagenticai.LLMS.groqllm import GroqLLM
from src.langgraphagenticai.graph.graph_builder import GraphBuilder
from src.langgraphagenticai.ui.streamlitui.display_result import DisplayResultStreamlit 


def load_langgraph_agenticai_app():
    """
    Loads and run the UI
    """

    ui = LoadStreamlitUI()
    user_input = ui.load_streamlit_ui()

    if not user_input:
        st.error("Error")

        return
    
    user_message = st.chat_input("Enter your Message")

    if user_message:
        try : 
            obj_llm_config = GroqLLM(user_controls_input=user_input)
            model = obj_llm_config.get_llm_model()

            if not model:
                st.error("Error: LLM Model could not be initialised")
                return
            
            usecase = user_input.get("selected_usecases")

            if not usecase:
                st.error("Error: No usecase selected.")

            graph_builder = GraphBuilder(model)

            try:
                graph = graph_builder.setup_graph(usecase)
                DisplayResultStreamlit(usecase,graph,user_message).display_result_on_ui()
            except Exception as e:
                st.error(f"Error: Graph Setup Failed- {e}")
                return
            


        except Exception as e:
            st.error(f"Error: Graph Setup Failed: {e}")
            return

       


    