from transformers import pipeline
import torch


class TestVQAModel:
    def test_predict(self):
        model_name = "stevhliu/my_awesome_wnut_model"
        device = "cuda" if torch.cuda.is_available() else "cpu"
        my_pipeline = pipeline("ner", model=model_name)
        input = 'The Golden State Warriors are an American professional basketball team based in San Francisco.'
        output = my_pipeline(input)
        
        assert type(output) == list

    
