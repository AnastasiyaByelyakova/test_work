from transformers import AutoTokenizer, AutoModel, pipeline
import torch
import re
from typing import Dict, List, Any
import numpy as np
from sentence_transformers import SentenceTransformer


class AbstractEmbedder:
    """Embed full abstracts using sentence transformers or SciBERT"""

    def __init__(self, model_name: str = "sentence-transformers/allenai-specter"):
        """
        Initialize abstract embedder

        Args:
            model_name: Choose from:
                - "sentence-transformers/allenai-specter" (recommended for scientific papers)
                - "sentence-transformers/all-MiniLM-L6-v2" (fast, general purpose)
                - "sentence-transformers/all-mpnet-base-v2" (high quality, general)
                - "allenai/scibert_scivocab_uncased" (scientific text)
        """
        # Try to use sentence-transformers if available, otherwise use transformers
        self.model = SentenceTransformer(model_name)
        self.use_sentence_transformer = True
        print(f"Loaded sentence-transformers model: {model_name}")

    def embed_abstract(self, paper_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Extract and embed abstract from paper data

        Returns:
            Dictionary with abstract text and embedding
        """
        # Find abstract field
        return self.model.encode(paper_data['abstract'],
                                 convert_to_numpy=True)


# ============================================================================
# USAGE EXAMPLE
# ============================================================================

if __name__ == "__main__":

    print("=" * 60)
    print("INITIALIZING MODULES")
    print("=" * 60)

    # Initialize both modules separately
    abstract_embedder = AbstractEmbedder()

    # Your paper data
    paper = {
        'authors': ['Leiner A. Suárez-Martínez', 'Edwin Bedoya-Roqueme', 'Jorge A. Quirós-Rodríguez'],
        'keywords': ['Arachnida', 'Neotropics', 'dry Forest', 'taxonomy', 'zoogeography'],
        'title': 'A new species of jumping spider of the genus Noegus Simon 1900 (Araneae: Salticidae: Amycini) from Colombia',
        'abstract': 'A new salticid species of the genus Noegus Simon 1900 is described herein as N. sombrerovueltiao sp. nov. (♂♀), found in the dry forest of the Córdoba department in northwestern Colombia. Photographs and illustrations of the diagnostic characters for males and females and ecological comments are provided. Distribution maps and habitat photographs are also included.',
        'topics': ['TAXONOMY'],
        'published': '2025-08-19T00:00:00.000+00:00'
    }

    # ========================================================================
    # MODULE 2: Embed abstract
    # ========================================================================
    print("\n" + "=" * 60)
    print( "ABSTRACT EMBEDDING (SPECTER)")
    print("=" * 60)

    abstract_results = abstract_embedder.embed_abstract(paper)

    print(f"\n📄 Abstract Text:")
    print(f"   Length: {len(abstract_results)}")

