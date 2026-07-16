class NuvioSocialMrrUpdaterClient:
    def format_bio(self, current_mrr: float, base_bio_template: str) -> dict:
        formatted_mrr = f"${current_mrr:,.0f}"
        return {"updated_bio_text": base_bio_template.replace("{MRR}", formatted_mrr)}