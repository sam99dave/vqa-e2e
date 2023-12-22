from transformers import pipeline
import torch


class VQAModel:
    def __init__(self, model_name: str = "stevhliu/my_awesome_wnut_model"):
        self.model_name = model_name
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.my_pipeline = pipeline("ner", model=self.model_name)
        # if pipeline:
        #     self.pipeline = pipeline("ner", model = model_name)
        # else:
        #     self.model, self.processor = self.get_model()

    def predict(self, input):
        output = self.my_pipeline(input)
        print(f"output: {output}")
        return output

    # def get_model(self):
    #     _model = VisionEncoderDecoderModel.from_pretrained(self.model_name)
    #     _processor = DonutProcessor.from_pretrained(self.model_name)

    #     return _model.to(self.device), _processor

    # def process_input(self, input_image, input_question):
    #     pixel_values = self.processor(input_image, return_tensors="pt").pixel_values
    #     decoder_input_ids = self.processor.tokenizer(
    #         input_question, add_special_tokens=False, return_tensors="pt"
    #     )["input_ids"]
    #     return pixel_values, decoder_input_ids

    # def post_process(self, output):
    #     seq = self.processor.batch_decode(output.sequences)[0]
    #     seq = seq.replace(self.processor.tokenizer.eos_token, "").replace(
    #         self.processor.tokenizer.pad_token, ""
    #     )
    #     seq = re.sub(
    #         r"<.*?>", "", seq, count=1
    #     ).strip()  # remove first task start token
    #     return self.processor.token2json(seq)

    # def predict(self, input_image, input_question):
    #     pixel_values, decoder_input_ids = self.process_input(input_image)
    #     outputs = self.model.generate(
    #         pixel_values.to(self.device),
    #         decoder_input_ids=decoder_input_ids.to(self.device),
    #         max_length=self.model.decoder.config.max_position_embeddings,
    #         early_stopping=True,
    #         pad_token_id=self.processor.tokenizer.pad_token_id,
    #         eos_token_id=self.processor.tokenizer.eos_token_id,
    #         use_cache=True,
    #         num_beams=1,
    #         bad_words_ids=[[self.processor.tokenizer.unk_token_id]],
    #         return_dict_in_generate=True,
    #         output_scores=True,
    #     )

    #     return self.post_process(outputs)


# m = VQAModel()
# print(m)
