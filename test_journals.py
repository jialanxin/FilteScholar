import unittest
from main import filter_paragraphs_containing_keywords, save_to_markdown

class TestJournals(unittest.TestCase): 
    def test_nature(self):
        sample_text = """[HTML] An atomically controlled insulator-to-metal transition in iridate/manganite heterostructures
E Men, D Li, H Zhang, J Chen, Z Qiao, L Wei, Z Wang… - Nature Communications, 2024
All-insulator heterostructures with an emerging metallicity are at the forefront of material science, which typically contain at least one band insulator while it is not necessary to be. Here we show emergent phenomena in a series of all-correlated …"""
        paragraphs = [sample_text]
        result = filter_paragraphs_containing_keywords(paragraphs)
        self.assertIn('Nature', result)

    def test_science(self):
        sample_text = """Bright dipolar excitons in twisted black phosphorus homostructures
S Huang, B Yu, Y Ma, C Pan, J Ma, Y Zhou, Y Ma… - Science, 2024
Bright dipolar excitons, which contain electrical dipoles and have high oscillator strength, are an ideal platform for studying correlated quantum phenomena. They usually rely on carrier tunneling between two quantum wells or two layers to …"""
        paragraphs = [sample_text]
        result = filter_paragraphs_containing_keywords(paragraphs)
        self.assertIn('Science', result)

    def test_science_advances(self):
        sample_text = """[HTML] Van der Waals integrated single-junction light-emitting diodes exceeding 10% quantum efficiency at room temperature
Z Hu, Q Fu, J Lu, Y Zhang, Q Zhang, S Wang, Z Duan… - Science Advances, 2024
The construction of miniaturized light-emitting diodes (LEDs) with high external quantum efficiency (EQE) at room temperature remains a challenge for on-chip optoelectronics. Here, we demonstrate microsized LEDs fabricated by a dry-transfer …."""
        paragraphs = [sample_text]
        result = filter_paragraphs_containing_keywords(paragraphs)
        self.assertIn('Science', result)

    def test_advanced_materials(self):
        sample_text = """[PDF] On‐Chip Synthesis of Quasi‐2D Semimetals from Multi‐Layer Chalcogenides
J Cai, H Zhang, Y Tan, Z Sun, P Wu, R Tripathi… - Advanced Materials, 2024
Reducing the dimensions of materials from three to two, or quasi‐two, provides a fertile platform for exploring emergent quantum phenomena and developing next‐generation electronic devices. However, growing high‐quality, ultrathin, quasi2D …
"""
        paragraphs = [sample_text]
        result = filter_paragraphs_containing_keywords(paragraphs)
        self.assertIn('Advanced Materials', result)

    def test_advanced_functional_materials(self):
        sample_text = """Reconfigurable van der Waals Ferroionic Barristor for Multifunctional Nanoelectronics
J Ding, R Cheng, Y Hou, Y Wang, L Yin, Y Wen… - Advanced Functional …, 2024
Abstract 2D materials have been interested in recent years due to their unique properties and enormous potential in various fields. In particular, 2D ferroionics with both ferroelectricity and ionic conductivity shed light on new possibilities for van der …"""
        paragraphs = [sample_text]
        result = filter_paragraphs_containing_keywords(paragraphs)
        self.assertIn('Advanced Materials', result)

    def test_arxiv(self):
        sample_text = """[PDF] A 5T-2MTJ STT-assisted Spin Orbit Torque based Ternary Content Addressable Memory for Hardware Accelerators
S Narla, P Kumar, A Naeemi - arXiv preprint arXiv:2409.17863, 2024
In this work, we present a novel non-volatile spin transfer torque (STT) assisted spin-orbit torque (SOT) based ternary content addressable memory (TCAM) with 5 transistors and 2 magnetic tunnel junctions (MTJs). We perform a comprehensive …"""
        paragraphs = [sample_text]
        result = filter_paragraphs_containing_keywords(paragraphs)
        self.assertIn('arXiv', result)

    def test_physical_review_x(self):
        sample_text = """[HTML] A new article has been accepted in Physical Review X.
E Men, D Li, H Zhang… - Physical Review X, 2024
This article discusses recent advancements in quantum mechanics."""
        paragraphs = [sample_text]
        result = filter_paragraphs_containing_keywords(paragraphs)
        self.assertIn('Physical Review X', result)

    def test_physical_review_letters(self):
        sample_text = """Ferroelectric Semimetals with α-Bi/SnSe van der Waals Heterostructures and Their Topological Currents
DJP De Sousa, S Lee, Q Lu, RG Moore, M Brahlek… - Physical Review Letters, 2024
We show that proximity effects can be utilized to engineer van der Waals heterostructures (vdWHs) displaying semimetallic spin-ferroelectricity locking, where ferroelectricity and semimetallic spin states are confined to different layers, but are …"""
        paragraphs = [sample_text]
        result = filter_paragraphs_containing_keywords(paragraphs)
        self.assertIn('Physical Review Letters', result)

    def test_nano_letters(self):
        sample_text = """Sub-THz High Spin Precession Frequency in van der Waals Ferromagnet Fe3GaTe2
J Zhang, Z Wang, Z Li, T Li, S Liu, J Zhang, RJ Zhang… - Nano Letters, 2024
The 2D magnet Fe3GaTe2 has received considerable attention for its high Curie temperature (TC), robust intrinsic ferromagnetism, and significant perpendicular magnetic anisotropy (PMA). In this study, the dynamic magnetic properties of …"""
        paragraphs = [sample_text]
        result = filter_paragraphs_containing_keywords(paragraphs)
        self.assertIn('Nano Letters', result)

    def test_acs_nano(self):
        sample_text = """[HTML] Atomically Precise Control of Topological State Hybridization in Conjugated Polymers
A Jiménez-Martín, Z Sosnová, D Soler, B Mallada… - ACS nano, 2024
Realization of topological quantum states in carbon nanostructures has recently emerged as a promising platform for hosting highly coherent and controllable quantum dot spin qubits. However, their adjustable manipulation remains elusive …"""
        paragraphs = [sample_text]
        result = filter_paragraphs_containing_keywords(paragraphs)
        self.assertIn('ACS Nano', result)

    def test_acs_nano_different_case(self):
        sample_text = """Light-Induced Ultrafast Glide-Mirror Symmetry Breaking in Black Phosphorus
C Bao, F Wang, H Zhong, S Zhou, T Lin, H Zhang… - ACS Nano, 2024
Symmetry breaking plays an important role in the fields of physics, ranging from particle physics to condensed matter physics. In solid-state materials, phase transitions are deeply linked to the underlying symmetry breakings, resulting in a rich …"""
        paragraphs = [sample_text]
        result = filter_paragraphs_containing_keywords(paragraphs)
        self.assertIn('ACS Nano', result)

    # Negative test cases for excluded journals
    def test_avs_quantum_science(self):
        sample_text = """Higher-fold topological excitations in phononic and electronic phases of chiral-type BaXY (X= Pt, Pd; Y= P, As, Sb, Bi) materials: A first-principles investigation
B Paul, S PC, RAB Villaos, ZQ Huang, H Lin… - AVS Quantum Science, 2025
Non-symmorphic chiral crystals hosting higher-fold fermions and bosons are of great interest due to the recent experimental realizations. The specialty of these higher-fold fermions and bosons is that they possess long Fermi arcs connecting the Brillouin …"""
        paragraphs = [sample_text]
        result = filter_paragraphs_containing_keywords(paragraphs)
        self.assertNotIn('Science', result)

    def test_small_science(self):
        sample_text = """[HTML] A new study on the effects of quantum entanglement
E Men, D Li, H Zhang… - Small Science, 2024
This study explores the implications of quantum entanglement in modern physics."""
        paragraphs = [sample_text]
        result = filter_paragraphs_containing_keywords(paragraphs)
        self.assertNotIn('Science', result)

    def test_journal_of_applied_science(self):
        sample_text = """[HTML] Advances in semiconductor technology
J Doe, A Smith… - Journal of Applied Science, 2024
This paper discusses recent advancements in semiconductor technology."""
        paragraphs = [sample_text]
        result = filter_paragraphs_containing_keywords(paragraphs)
        self.assertNotIn('Science', result)

    def test_science_and_technology(self):
        sample_text = """[HTML] Innovations in material science
A Johnson… - Science & Technology, 2024
This article reviews innovations in material science."""
        paragraphs = [sample_text]
        result = filter_paragraphs_containing_keywords(paragraphs)
        self.assertNotIn('Science', result)

    def test_advanced_science(self):
        sample_text = """[HTML] New approaches in nanotechnology
B Lee… - Advanced Science, 2024
This research presents new approaches in nanotechnology."""
        paragraphs = [sample_text]
        result = filter_paragraphs_containing_keywords(paragraphs)
        self.assertNotIn('Science', result)
        self.assertNotIn('Advance Materials', result)

    # New negative test case for "Advanced Materials Technologies"
    def test_advanced_materials_technologies(self):
        sample_text = """[HTML] Innovations in advanced materials
C Smith… - Advanced Materials Technologies, 2024
This paper discusses innovations in advanced materials technologies."""
        paragraphs = [sample_text]
        result = filter_paragraphs_containing_keywords(paragraphs)
        self.assertNotIn('Advanced Materials', result)

    def test_progress_in_natural_science(self):
        sample_text = """Regulation of charge density wave and superconductivity in kagome superconductor CsV3Sb5 by intercalation
H Xiao, Y Zhang, L Yu, M Mi, X Liu, Q Cui, B Lyu, Y Guo… - Progress in Natural Science …, 2024
Abstract AV 3 Sb 5 (A​=​ K, Rb, and Cs), recently discovered van der Waals Kagome metals, exhibit a multitude of intriguing strongly correlated phenomena, particularly the unconventional charge density wave (CDW) and superconductivity …"""
        paragraphs = [sample_text]
        result = filter_paragraphs_containing_keywords(paragraphs)
        self.assertNotIn('Science', result)

    def test_science_and_technology_of(self):
        sample_text = """[HTML] Metastable body-centered cubic CoMnFe alloy films with perpendicular magnetic anisotropy for spintronics memory
D Kumar, M Ishibashi, T Roy, M Tsujikawa, M Shirai… - Science and Technology of …, 2024
ABSTRACT A body-centered cubic (bcc) FeCo (B) is a current standard magnetic material for perpendicular magnetic tunnel junctions (p-MTJs) showing both large tunnel magnetoresistance (TMR) and high interfacial perpendicular magnetic …"""
        paragraphs = [sample_text]
        result = filter_paragraphs_containing_keywords(paragraphs)
        self.assertNotIn('Science', result)

    def test_light_science(self):
        sample_text = """[HTML] Simultaneous achieving negative photoconductivity response and volatile resistive switching in Cs2CoCl4 single crystals towards artificial optoelectronic synapse
H Jiang, H Ji, Z Ma, D Yang, J Ma, M Zhang, X Li… - Light: Science & …, 2024
The development of negative photoconductivity (NPC)-related devices is of great significance for numerous applications, such as optoelectronic detection, neuromorphic computing, and optoelectronic synapses. Here, an unusual but …"""
        paragraphs = [sample_text]
        result = filter_paragraphs_containing_keywords(paragraphs)
        self.assertNotIn('Science', result)

    def test_surface_science(self):
        sample_text = """Growth and electronic structure of the nodal line semimetal in monolayer Cu2Si on Cu (111)
J Xu, C Liu, Y Guo, G Zhang, K Liu, H Qian, K Nie… - Surface Science, 2024
Cu 2 Si, a single-layer two-dimensional material with a honeycomb structure, has been proposed to have Dirac nodal line fermions. In this study, the synchrotron radiation X-ray photoelectron spectroscopy, ultraviolet photoelectron spectroscopy …"""
        paragraphs = [sample_text]
        result = filter_paragraphs_containing_keywords(paragraphs)
        self.assertNotIn('Science', result)

    def test_superconductor_science(self):
        sample_text = """Phonon-mediated superconductivity in topological kagome metals Rh3M2S2 (M= Pb, In, Tl)
WY Liu, X Wang, Y Li, YH Wei, M Zhong, MQ Kuang - Superconductor Science and …, 2025
Kagome materials possess intriguing properties and have attracted considerable interest. Inspired by the extensive research on kagome superconductors, here, we investigated the superconducting and topological properties of the trilayer kagome …"""
        paragraphs = [sample_text]
        result = filter_paragraphs_containing_keywords(paragraphs)
        self.assertNotIn('Science', result)

    def test_cell_reports_physical_science(self):
        sample_text = """[HTML] Area-selective deposition of lateral van der Waals semiconductor heterostructures
CS Lee, HJ Han, JH Ahn, G Jin - Cell Reports Physical Science, 2024
Scalable area-selective deposition of van der Waals semiconductor monolayer enables the tunable design of atomically thin, two-dimensional electronic and photonic material platforms. Here, we report lateral patterning of tunable …"""
        paragraphs = [sample_text]
        result = filter_paragraphs_containing_keywords(paragraphs)
        self.assertNotIn('Science', result)

    def test_mechanics_of_advanced_materials(self):
        sample_text = """Dynamics of transverse domain wall in bilayer ferromagnetic-heavy metal nanostructures: Interplay of spin-orbit torque, dry-friction dissipation, and the interfacial …
A Halder, S Dolui, S Dwivedi - Mechanics of Advanced Materials and Structures, 2024
This work deals with the static and dynamic characteristics of the transverse Bloch domain wall within a bilayer nanostructure comprising a ferromagnetic layer and a non-magnetic heavy metal layer. We examine the spatiotemporal evolution of …"""
        paragraphs = [sample_text]
        result = filter_paragraphs_containing_keywords(paragraphs)
        self.assertNotIn('Advanced Materials', result)

    def test_nano_letters_case_insensitive(self):
        # 测试大小写不同的期刊名称
        sample_text_1 = """Sign Reversal of Hall Conductivity in Polycrystalline FeRh Films via the Topological Hall Effect in the Antiferromagnetic Phase
YH Kim, JW Choi, JM Cho, GS Kim, NW Park, G Park… - Nano letters, 2025
The intrinsic Berry curvature in ferromagnetic (FM) materials significantly influences Hall conductivity during the antiferromagnetic (AFM)-to-FM phase transition, as demonstrated through the anomalous Hall effect (AHE). First-principles calculations …"""
        paragraphs = [sample_text_1]
        result = filter_paragraphs_containing_keywords(paragraphs)
        self.assertIn('Nano Letters', result)


    def test_string_normalization(self):
        # 测试带有不同空白字符和换行符的相同文章
        sample_text_1 = """
Quantum Anomalous Layer Hall Effect in Realistic van der Waals Heterobilayers
Y Tian, X Kong, C Jiang, HJ Zhang, WJ Gong - Nano Letters, 2024
The quantum anomalous layer Hall effect (QALHE), characterized by the precise control of the quantum anomalous Hall effect on different layers due to spin-layer-chirality coupling in van der Waals (vdW) layered materials, is of great importance in …"""

        sample_text_2 = """Quantum Anomalous Layer Hall Effect in Realistic van der Waals Heterobilayers
Y Tian, X Kong, C Jiang, HJ Zhang, WJ Gong - Nano Letters, 2024
The quantum anomalous layer Hall effect (QALHE), characterized by the precise control of the quantum anomalous Hall effect on different layers due to spin-layer-chirality coupling in van der Waals (vdW) layered materials, is of great importance in …
"""
        # 处理两个样本
        result_1 = filter_paragraphs_containing_keywords([sample_text_1])
        result_2 = filter_paragraphs_containing_keywords([sample_text_2])

        # 获取 Nano Letters 中的文章集合
        articles_1 = result_1.get('Nano Letters', set())
        articles_2 = result_2.get('Nano Letters', set())

        # 验证两个集合的交集等于任意一个集合（即它们包含相同的元素）
        self.assertEqual(articles_1, articles_2, "带有不同空白字符的相同文章应该被识别为相同")

    def test_journal_sorting(self):
        # 准备测试数据
        test_paragraphs = {
            'Advanced Materials': {'para1', 'para2'},
            'Nano Letters': {'para3'},
            'Science': {'para4'},
            'arXiv': {'para5'},
            'Physical Review Letters': {'para6'},
            'Physical Review X': {'para7'},
            'Nature': {'para8'},
            'Other Journal': {'para9'}
        }
        
        # 调用保存方法
        save_to_markdown(test_paragraphs, "temp_test.md")
        
        # 验证文件内容顺序
        with open("temp_test.md", "r", encoding="utf-8") as f:
            content = f.read()
            
        # 检查标题顺序
        expected_order = [
            "# Science",
            "# Nature", 
            "# Physical Review X",
            "# Physical Review Letters",
            "# Advanced Materials",
            "# Nano Letters",
            "# arXiv",
            "# Other Journal"
        ]
        
        # 获取实际出现的标题
        actual_headings = [line for line in content.split('\n') if line.startswith('#')]
        
        # 验证顺序是否正确
        for expected, actual in zip(expected_order, actual_headings):
            self.assertEqual(actual, expected)
            
        # 清理临时文件
        import os
        os.remove("temp_test.md")

if __name__ == '__main__':
    unittest.main()
