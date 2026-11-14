from dataclasses import dataclass
from drafter import *


# GLOBAL CONSTANTS
# These lists are treated as constants and are not modified by the app.

CATEGORIES: list[str] = [
    "General / Intro Electives",
    "Computer Science & Data",
    "Mathematics & Statistics",
    "Engineering (ChemE, BMEG, EE, MechE)",
    "Physical Sciences (Chem & Physics)",
    "Biology & Pre-Med",
    "Nursing & Health Professions",
    "Business, Finance & Accounting",
    "Excel & Quantitative Spreadsheets",
    "Psychology, Social Sciences & Humanities",
]

PRIORITIES: list[str] = [
    "Highest Accuracy",
    "Fastest Speed",
    "Lowest Cost / Free",
]

RATINGS: list[str] = ["1", "2", "3", "4", "5"]

# Course keyword lists checked from most specific to most general
EXCEL_KEYWORDS: list[str] = [
    "excel", "spreadsheet", "vlookup", "xlookup", "pivot table", "macro",
    "vba", "conditional formatting", "index match", "workbook", "csv",
]

BUSINESS_KEYWORDS: list[str] = [
    "finance", "accounting", "balance sheet", "income statement", "cash flow",
    "npv", "irr", "wacc", "amortization", "depreciation", "journal entry",
    "debit", "credit", "roi", "dcf", "valuation", "gaap", "economics",
    "supply and demand", "marketing",
]

NURSING_HEALTH_KEYWORDS: list[str] = [
    "nursing", "nclex", "pharmacology", "pathophysiology", "dosage",
    "triage", "patient", "clinical", "vital signs", "care plan",
    "med-surg", "pediatric", "contraindication", "public health",
]

BIO_PREMED_KEYWORDS: list[str] = [
    "biology", "premed", "pre-med", "mcat", "genetics", "anatomy",
    "physiology", "neuroscience", "enzyme", "protein", "dna", "mrna",
    "transcription", "mitosis", "meiosis", "eukaryotic", "cellular",
    "biochemistry", "metabolism",
]

ENGINEERING_KEYWORDS: list[str] = [
    "engineering", "bmeg", "biomedical", "organoid", "biomaterial",
    "cytoskeletal", "cheme", "chemical engineering", "distillation",
    "mass balance", "energy balance", "heat transfer", "reactor",
    "circuit", "voltage", "resistor", "capacitor", "inductor", "gauss",
    "maxwell", "faraday", "thermodynamics", "matlab", "statics",
    "fluid mechanics",
]

PHYSICAL_SCIENCE_KEYWORDS: list[str] = [
    "chemistry", "stoichiometry", "limiting reactant", "molarity",
    "enthalpy", "entropy", "gibbs", "organic chemistry", "orgo", "titration",
    "acid-base", "reagent", "molecule", "physics", "kinematics", "optics",
    "electric field", "magnetic field", "quantum", "lab report",
]

MATH_STATS_KEYWORDS: list[str] = [
    "math", "solve", "equation", "differential equation", "laplace",
    "eigenvalue", "eigenvector", "proof", "calculate", "compute", "algebra",
    "calculus", "matrix", "determinant", "integral", "derivative",
    "probability", "statistics", "hypothesis test", "p-value", "regression",
    "theorem",
]

CS_DATA_KEYWORDS: list[str] = [
    "python", "code", "bug", "error", "function", "loop", "html", "java",
    "c++", "debug", "syntax", "class", "dataclass", "script", "program",
    "algorithm", "recursion", "sql", "database", "data structure",
]

HUMANITIES_SOCIAL_KEYWORDS: list[str] = [
    "psychology", "sociology", "history", "political science", "essay",
    "story", "write", "draft", "paragraph", "outline", "research",
    "source", "study", "paper", "cite", "citation", "apa", "mla",
    "summarize", "article", "literature review", "thesis",
]

# Triggers the +5 complexity bonus even when a prompt is under 20 words
HARD_TASK_KEYWORDS: list[str] = [
    "determinant", "matrix", "8x8", "differential equation", "laplace",
    "eigenvalue", "proof", "theorem", "integral", "derivative", "maxwell",
    "gauss", "faraday", "circuit analysis", "stoichiometry",
    "limiting reactant", "gibbs", "mass balance", "energy balance",
    "distillation", "heat transfer", "organoid", "biomaterial",
    "pharmacology", "pathophysiology", "dosage", "mcat", "nclex", "npv",
    "irr", "wacc", "dcf", "balance sheet", "pivot table", "xlookup",
    "vlookup", "vba", "architecture", "optimize", "algorithm", "recursion",
    "from scratch", "step-by-step", "regression",
]


# ==============================================================================
# DATACLASSES
# ==============================================================================

@dataclass
class ModelProfile:
    """Represents a single Large Language Model and its rubric attributes."""
    name: str
    best_category: str
    accuracy_rating: int
    speed_rating: int
    is_free: bool
    strengths: str
    last_score: int
    bonus_summary: str
    times_recommended: int


@dataclass
class EvaluationRecord:
    """Represents a user-submitted quality audit of an AI response."""
    model_name: str
    category: str
    prompt_tested: str
    response_snippet: str
    accuracy_score: int
    clarity_score: int
    fact_checked: bool
    trust_label: str


@dataclass
class State:
    """Stores persistent application data across all pages and routes."""
    user_prompt: str
    selected_category: str
    selected_priority: str
    recommended_model_name: str
    recommendation_reason: str
    winner_math_steps: list[str]
    keyword_feedback: str
    complexity_feedback: str
    models: list[ModelProfile]
    evaluations: list[EvaluationRecord]


# ==============================================================================
# INITIALIZATION HELPER FUNCTIONS
# ==============================================================================

def create_initial_models() -> list[ModelProfile]:
    """Creates 20 predefined ModelProfile instances across all 10 tracks."""
    return [
        ModelProfile(
            name="GPT-4o",
            best_category="General / Intro Electives",
            accuracy_rating=9,
            speed_rating=9,
            is_free=False,
            strengths="Well-rounded explanations, brainstorming, and electives.",
            last_score=0,
            bonus_summary="None",
            times_recommended=0,
        ),
        ModelProfile(
            name="Phi-4 (14B)",
            best_category="General / Intro Electives",
            accuracy_rating=8,
            speed_rating=10,
            is_free=True,
            strengths="Fast, free open-weights study helper for intro courses.",
            last_score=0,
            bonus_summary="None",
            times_recommended=0,
        ),
        ModelProfile(
            name="Claude Sonnet 4.6",
            best_category="Computer Science & Data",
            accuracy_rating=10,
            speed_rating=7,
            is_free=False,
            strengths="Software debugging, data structures, and walkthroughs.",
            last_score=0,
            bonus_summary="None",
            times_recommended=0,
        ),
        ModelProfile(
            name="Qwen 3.8 (27B)",
            best_category="Computer Science & Data",
            accuracy_rating=9,
            speed_rating=9,
            is_free=True,
            strengths="Fast, free open-weights coding, SQL, and algorithms.",
            last_score=0,
            bonus_summary="None",
            times_recommended=0,
        ),
        ModelProfile(
            name="DeepSeek-R1",
            best_category="Mathematics & Statistics",
            accuracy_rating=10,
            speed_rating=6,
            is_free=True,
            strengths="Symbolic reasoning for linear algebra, ODEs, and proofs.",
            last_score=0,
            bonus_summary="None",
            times_recommended=0,
        ),
        ModelProfile(
            name="GLM-5.3-Flash",
            best_category="Mathematics & Statistics",
            accuracy_rating=9,
            speed_rating=9,
            is_free=True,
            strengths="Fast calculus, probability, and hypothesis tests.",
            last_score=0,
            bonus_summary="None",
            times_recommended=0,
        ),
        ModelProfile(
            name="OpenAI o3-mini",
            best_category="Engineering (ChemE, BMEG, EE, MechE)",
            accuracy_rating=10,
            speed_rating=7,
            is_free=True,
            strengths="Derivations for E&M circuits, mass balances, and BMEG.",
            last_score=0,
            bonus_summary="None",
            times_recommended=0,
        ),
        ModelProfile(
            name="Mistral Small 4",
            best_category="Engineering (ChemE, BMEG, EE, MechE)",
            accuracy_rating=8,
            speed_rating=9,
            is_free=True,
            strengths="Fast open-weights model for MATLAB and unit checks.",
            last_score=0,
            bonus_summary="None",
            times_recommended=0,
        ),
        ModelProfile(
            name="Claude Opus 4.6",
            best_category="Physical Sciences (Chem & Physics)",
            accuracy_rating=10,
            speed_rating=6,
            is_free=False,
            strengths="Precision on stoichiometry, mechanisms, and physics.",
            last_score=0,
            bonus_summary="None",
            times_recommended=0,
        ),
        ModelProfile(
            name="DeepSeek-V4",
            best_category="Physical Sciences (Chem & Physics)",
            accuracy_rating=9,
            speed_rating=8,
            is_free=True,
            strengths="Free open-weights model for thermo and equilibrium.",
            last_score=0,
            bonus_summary="None",
            times_recommended=0,
        ),
        ModelProfile(
            name="Gemini 2.5 Pro",
            best_category="Biology & Pre-Med",
            accuracy_rating=9,
            speed_rating=8,
            is_free=True,
            strengths="Genetics, cellular pathways, and MCAT passages.",
            last_score=0,
            bonus_summary="None",
            times_recommended=0,
        ),
        ModelProfile(
            name="Llama 4 Maverick",
            best_category="Biology & Pre-Med",
            accuracy_rating=8,
            speed_rating=9,
            is_free=True,
            strengths="Fast open-weights helper for anatomy and bio guides.",
            last_score=0,
            bonus_summary="None",
            times_recommended=0,
        ),
        ModelProfile(
            name="GPT-5.1",
            best_category="Nursing & Health Professions",
            accuracy_rating=10,
            speed_rating=8,
            is_free=False,
            strengths="Clinical reasoning for pharmacology and NCLEX prep.",
            last_score=0,
            bonus_summary="None",
            times_recommended=0,
        ),
        ModelProfile(
            name="Gemma 4 (31B)",
            best_category="Nursing & Health Professions",
            accuracy_rating=8,
            speed_rating=10,
            is_free=True,
            strengths="Ultra-fast open model for dosage checks and study cards.",
            last_score=0,
            bonus_summary="None",
            times_recommended=0,
        ),
        ModelProfile(
            name="OpenAI o4-mini",
            best_category="Business, Finance & Accounting",
            accuracy_rating=9,
            speed_rating=8,
            is_free=False,
            strengths="Corporate finance (NPV/WACC), GAAP entries, valuation.",
            last_score=0,
            bonus_summary="None",
            times_recommended=0,
        ),
        ModelProfile(
            name="Qwen 3 (14B)",
            best_category="Business, Finance & Accounting",
            accuracy_rating=8,
            speed_rating=10,
            is_free=True,
            strengths="Fast open model for economics and financial ratios.",
            last_score=0,
            bonus_summary="None",
            times_recommended=0,
        ),
        ModelProfile(
            name="GPT-4.1",
            best_category="Excel & Quantitative Spreadsheets",
            accuracy_rating=10,
            speed_rating=8,
            is_free=False,
            strengths="Nested Excel formulas (XLOOKUP, INDEX/MATCH) and VBA.",
            last_score=0,
            bonus_summary="None",
            times_recommended=0,
        ),
        ModelProfile(
            name="Llama 4 Scout",
            best_category="Excel & Quantitative Spreadsheets",
            accuracy_rating=8,
            speed_rating=9,
            is_free=True,
            strengths="Fast open-weights helper for spreadsheets and CSVs.",
            last_score=0,
            bonus_summary="None",
            times_recommended=0,
        ),
        ModelProfile(
            name="Kimi K3 (Open-Weights)",
            best_category="Psychology, Social Sciences & Humanities",
            accuracy_rating=9,
            speed_rating=7,
            is_free=True,
            strengths="Long-context literature reviews, APA/MLA, and essays.",
            last_score=0,
            bonus_summary="None",
            times_recommended=0,
        ),
        ModelProfile(
            name="Gemini 2.5 Flash",
            best_category="Psychology, Social Sciences & Humanities",
            accuracy_rating=8,
            speed_rating=10,
            is_free=True,
            strengths="Instant lecture summaries, study guides, and reviews.",
            last_score=0,
            bonus_summary="None",
            times_recommended=0,
        ),
    ]


def create_initial_state() -> State:
    """Creates a clean initial State dataclass instance."""
    return State(
        user_prompt="",
        selected_category=CATEGORIES[0],
        selected_priority=PRIORITIES[0],
        recommended_model_name="",
        recommendation_reason="",
        winner_math_steps=[],
        keyword_feedback="",
        complexity_feedback="",
        models=create_initial_models(),
        evaluations=[],
    )


# ==============================================================================
# KEYWORD & COMPLEXITY HELPER FUNCTIONS (Each returns one simple value)
# ==============================================================================

def contains_any_keyword(text: str, keywords: list[str]) -> bool:
    """Returns True if any keyword from the list appears in text."""
    for word in keywords:
        if word in text:
            return True
    return False


def get_first_matching_keyword(text: str, keywords: list[str]) -> str:
    """Returns the first keyword from the list found in text, or empty string."""
    for word in keywords:
        if word in text:
            return word
    return ""


def find_keyword_category(prompt: str) -> str:
    """Returns the academic category matching keywords in prompt, or empty string."""
    lower_prompt: str = prompt.lower()

    if contains_any_keyword(lower_prompt, EXCEL_KEYWORDS):
        return "Excel & Quantitative Spreadsheets"
    if contains_any_keyword(lower_prompt, BUSINESS_KEYWORDS):
        return "Business, Finance & Accounting"
    if contains_any_keyword(lower_prompt, NURSING_HEALTH_KEYWORDS):
        return "Nursing & Health Professions"
    if contains_any_keyword(lower_prompt, BIO_PREMED_KEYWORDS):
        return "Biology & Pre-Med"
    if contains_any_keyword(lower_prompt, ENGINEERING_KEYWORDS):
        return "Engineering (ChemE, BMEG, EE, MechE)"
    if contains_any_keyword(lower_prompt, PHYSICAL_SCIENCE_KEYWORDS):
        return "Physical Sciences (Chem & Physics)"
    if contains_any_keyword(lower_prompt, MATH_STATS_KEYWORDS):
        return "Mathematics & Statistics"
    if contains_any_keyword(lower_prompt, CS_DATA_KEYWORDS):
        return "Computer Science & Data"
    if contains_any_keyword(lower_prompt, HUMANITIES_SOCIAL_KEYWORDS):
        return "Psychology, Social Sciences & Humanities"

    return ""


def find_matched_keyword(prompt: str) -> str:
    """Returns the specific keyword found in prompt, or empty string."""
    lower_prompt: str = prompt.lower()
    all_lists: list[list[str]] = [
        EXCEL_KEYWORDS,
        BUSINESS_KEYWORDS,
        NURSING_HEALTH_KEYWORDS,
        BIO_PREMED_KEYWORDS,
        ENGINEERING_KEYWORDS,
        PHYSICAL_SCIENCE_KEYWORDS,
        MATH_STATS_KEYWORDS,
        CS_DATA_KEYWORDS,
        HUMANITIES_SOCIAL_KEYWORDS,
    ]
    for keyword_list in all_lists:
        matched: str = get_first_matching_keyword(lower_prompt, keyword_list)
        if matched != "":
            return matched
    return ""


def is_complex_prompt(prompt: str) -> bool:
    """Returns True if prompt has 20+ words or contains an advanced term."""
    word_count: int = len(prompt.split())
    if word_count >= 20:
        return True

    lower_prompt: str = prompt.lower()
    if contains_any_keyword(lower_prompt, HARD_TASK_KEYWORDS):
        return True

    return False


def describe_prompt_complexity(prompt: str) -> str:
    """Returns a readable explanation of whether the prompt earned a bonus."""
    word_count: int = len(prompt.split())
    if word_count >= 20:
        return (
            str(word_count)
            + " words (meets 20+ word threshold) -> +5 bonus for accuracy >= 9."
        )

    lower_prompt: str = prompt.lower()
    hard_word: str = get_first_matching_keyword(lower_prompt, HARD_TASK_KEYWORDS)
    if hard_word != "":
        return (
            str(word_count)
            + " words, detected advanced term '"
            + hard_word
            + "' -> +5 bonus for accuracy >= 9."
        )

    return str(word_count) + " words (concise prompt, no extra complexity bonus)."


# ==============================================================================
# SCORING, RANKING & LABEL HELPER FUNCTIONS
# ==============================================================================

def format_access_label(is_free: bool) -> str:
    """Converts a boolean is_free flag into a readable access tier string."""
    if is_free:
        return "Free / Open"
    return "Paid Tier"


def get_all_model_names(models: list[ModelProfile]) -> list[str]:
    """Returns a list of all model names for dropdown menus."""
    names: list[str] = []
    for model in models:
        names.append(model.name)
    return names


def calculate_model_score(
    model: ModelProfile,
    category: str,
    priority: str,
    complex_task: bool,
    keyword_category: str,
) -> int:
    """Calculates and returns the total integer rubric score for one model."""
    score: int = 0

    if model.best_category == category:
        score = score + 15
    else:
        score = score + 5

    if keyword_category != "" and model.best_category == keyword_category:
        score = score + 8

    if complex_task and model.accuracy_rating >= 9:
        score = score + 5

    if priority == "Highest Accuracy":
        score = score + (model.accuracy_rating * 3)
    elif priority == "Fastest Speed":
        score = score + (model.speed_rating * 3)
    elif priority == "Lowest Cost / Free":
        if model.is_free:
            score = score + 25 + model.accuracy_rating
        else:
            score = score - 10

    return score


def summarize_model_bonuses(
    model: ModelProfile,
    complex_task: bool,
    keyword_category: str,
) -> str:
    """Returns a short string showing which extra bonuses a model earned."""
    has_keyword: bool = (
        keyword_category != "" and model.best_category == keyword_category
    )
    has_complexity: bool = complex_task and model.accuracy_rating >= 9

    if has_keyword and has_complexity:
        return "+8 Keyword, +5 Complexity"
    if has_keyword:
        return "+8 Keyword"
    if has_complexity:
        return "+5 Complexity"
    return "None"


def explain_model_score(
    model: ModelProfile,
    category: str,
    priority: str,
    complex_task: bool,
    keyword_category: str,
) -> list[str]:
    """Returns a list of step-by-step strings explaining a model's score."""
    steps: list[str] = []

    if model.best_category == category:
        steps.append(
            "Category Match (+15 pts): Specializes in " + model.best_category
        )
    else:
        steps.append(
            "Cross-Domain Fit (+5 pts): General support outside " + category
        )

    if keyword_category != "" and model.best_category == keyword_category:
        steps.append(
            "Keyword Clue Bonus (+8 pts): Prompt matched " + keyword_category
        )

    if complex_task and model.accuracy_rating >= 9:
        steps.append(
            "Complexity Bonus (+5 pts): High-accuracy model ("
            + str(model.accuracy_rating)
            + "/10) for advanced task"
        )

    if priority == "Highest Accuracy":
        accuracy_points: int = model.accuracy_rating * 3
        steps.append(
            "Accuracy Priority (+"
            + str(accuracy_points)
            + " pts): Rating "
            + str(model.accuracy_rating)
            + "/10 x 3"
        )
    elif priority == "Fastest Speed":
        speed_points: int = model.speed_rating * 3
        steps.append(
            "Speed Priority (+"
            + str(speed_points)
            + " pts): Rating "
            + str(model.speed_rating)
            + "/10 x 3"
        )
    elif priority == "Lowest Cost / Free":
        if model.is_free:
            free_points: int = 25 + model.accuracy_rating
            steps.append(
                "Free Access Priority (+"
                + str(free_points)
                + " pts): +25 Free bonus + "
                + str(model.accuracy_rating)
                + " Accuracy"
            )
        else:
            steps.append(
                "Paid Tier Penalty (-10 pts): User requested Lowest Cost / Free"
            )

    return steps


def get_top_five_by_score(models: list[ModelProfile]) -> list[ModelProfile]:
    """Selects up to 5 models with the highest last_score using simple loops."""
    top_models: list[ModelProfile] = []
    used_names: list[str] = []

    while len(top_models) < 5 and len(top_models) < len(models):
        best_model: ModelProfile = models[0]
        best_score: int = -9999
        for model in models:
            if model.name not in used_names:
                if model.last_score > best_score:
                    best_score = model.last_score
                    best_model = model
        top_models.append(best_model)
        used_names.append(best_model.name)

    return top_models


def get_top_five_by_recommendations(
    models: list[ModelProfile],
) -> list[ModelProfile]:
    """Returns up to five models that have been recommended."""
    top_models: list[ModelProfile] = []
    used_names: list[str] = []

    while len(top_models) < 5:
        best_model: ModelProfile = models[0]
        best_count: int = 0
        for model in models:
            if model.name not in used_names:
                if model.times_recommended > best_count:
                    best_count = model.times_recommended
                    best_model = model
        if best_count == 0:
            break
        top_models.append(best_model)
        used_names.append(best_model.name)

    return top_models


def determine_trust_verdict(
    accuracy_score: int, clarity_score: int, fact_checked: bool
) -> str:
    """Assigns a readable trust label based on user ratings and verification."""
    if accuracy_score >= 4 and clarity_score >= 4 and fact_checked:
        return "High Trust (Verified)"
    if accuracy_score >= 3 and clarity_score >= 3:
        return "Moderate Trust (Double-Check Details)"
    return "Low Trust (Needs Revision)"


def build_explanation(model: ModelProfile, category: str, priority: str) -> str:
    """Generates a concise summary explaining why the winning model ranked #1."""
    cost_text: str = format_access_label(model.is_free)
    fit_note: str = "offers strong cross-domain support for " + category
    if model.best_category == category:
        fit_note = "specializes in " + category

    return (
        model.name
        + " ("
        + cost_text
        + ") ranked #1 with "
        + str(model.last_score)
        + " points because it "
        + fit_note
        + " and fits your priority of '"
        + priority
        + "'. Key strength: "
        + model.strengths
    )


# ==============================================================================
# TABLE BUILDER HELPER FUNCTIONS (Builds rows cleanly one list at a time)
# ==============================================================================

def build_top_five_table(top_models: list[ModelProfile]) -> Table:
    """Builds the Top 5 ranked comparison Table from a list of models."""
    header_row: list[str] = [
        "Rank",
        "Model Name",
        "Major Track",
        "Accuracy",
        "Speed",
        "Cost",
        "Bonuses",
        "Total Score",
    ]
    rows: list[list[str]] = [header_row]

    rank_number: int = 1
    for model in top_models:
        row: list[str] = [
            "#" + str(rank_number),
            model.name,
            model.best_category,
            str(model.accuracy_rating) + "/10",
            str(model.speed_rating) + "/10",
            format_access_label(model.is_free),
            model.bonus_summary,
            str(model.last_score) + " pts",
        ]
        rows.append(row)
        rank_number = rank_number + 1

    return Table(rows)


def build_evaluations_table(evaluations: list[EvaluationRecord]) -> Table:
    """Builds the saved answer evaluations Table from EvaluationRecord items."""
    header_row: list[str] = [
        "Model",
        "Category",
        "Prompt Tested",
        "Response Snippet",
        "Accuracy",
        "Clarity",
        "Verified",
        "Verdict",
    ]
    rows: list[list[str]] = [header_row]

    for record in evaluations:
        verified_text: str = "No"
        if record.fact_checked:
            verified_text = "Yes"

        row: list[str] = [
            record.model_name,
            record.category,
            record.prompt_tested,
            record.response_snippet,
            str(record.accuracy_score) + "/5",
            str(record.clarity_score) + "/5",
            verified_text,
            record.trust_label,
        ]
        rows.append(row)

    return Table(rows)


def build_leaderboard_table(top_models: list[ModelProfile]) -> Table:
    """Builds the Top 5 most-recommended models leaderboard Table."""
    header_row: list[str] = [
        "Rank",
        "Model Name",
        "Major Track",
        "Access",
        "Times Recommended",
    ]
    rows: list[list[str]] = [header_row]

    rank_number: int = 1
    for model in top_models:
        row: list[str] = [
            "#" + str(rank_number),
            model.name,
            model.best_category,
            format_access_label(model.is_free),
            str(model.times_recommended),
        ]
        rows.append(row)
        rank_number = rank_number + 1

    return Table(rows)


def build_baseline_models_table(models: list[ModelProfile]) -> Table:
    """Builds the baseline ratings reference Table for all 20 models."""
    header_row: list[str] = [
        "Model Name",
        "Major Track",
        "Accuracy",
        "Speed",
        "Access",
        "Key Strength",
    ]
    rows: list[list[str]] = [header_row]

    for model in models:
        row: list[str] = [
            model.name,
            model.best_category,
            str(model.accuracy_rating) + "/10",
            str(model.speed_rating) + "/10",
            format_access_label(model.is_free),
            model.strengths,
        ]
        rows.append(row)

    return Table(rows)


# ==============================================================================
# PAGE RENDERING FUNCTIONS (6 Distinct Pages)
# ==============================================================================

def render_home_page(state: State) -> Page:
    """Page 1: Landing page introducing the router and supported tracks."""
    tracks_list: list[str] = [
        "General / Intro Electives (Broad Study Guides, Brainstorming, Surveys)",
        "Computer Science & Data (Python, Java, C++, SQL, Algorithms)",
        "Mathematics & Statistics (Calculus, Linear Algebra, Diff Eq)",
        "Engineering: ChemE, BMEG, EE, MechE (Circuits, Mass Balances)",
        "Physical Sciences: Chem & Physics (Stoichiometry, Orgo, Optics)",
        "Biology & Pre-Med (Genetics, Anatomy, Cellular Pathways, MCAT)",
        "Nursing & Health Professions (Pharmacology, Dosage Math, NCLEX)",
        "Business, Finance & Accounting (NPV/WACC, GAAP Balance Sheets)",
        "Excel & Quantitative Spreadsheets (XLOOKUP, Pivot Tables, VBA)",
        "Psychology, Social Sciences & Humanities (Lit Reviews, APA/MLA)",
    ]

    return Page(
        state,
        [
            Header("College AI Model Router & Answer Quality Evaluator"),
            "Compare 20 LLMs across 10 undergraduate tracks using a transparent "
            "point rubric, see the step-by-step math behind each pick, and log "
            "quality audits of AI responses.",
            LineBreak(),
            Div(
                bold("Disclaimer: "),
                "Model ratings and access information are predefined estimates "
                "used for this educational comparison. Rankings are calculated "
                "using the application's scoring formula and are not live "
                "benchmark results. Model capabilities, availability, and "
                "pricing may change. Always verify important information with "
                "the provider.",
            ),
            LineBreak(),
            bold("Supported Undergraduate Tracks:"),
            BulletedList(tracks_list),
            HorizontalRule(),
            Button("Start Model Selection", "go_to_input"),
            Button("View Scoring & Trust Rubric", "go_to_rubric"),
            Button("View Saved Evaluations & Leaderboard", "go_to_history"),
        ],
    )


def render_input_page(state: State, error_message: str = "") -> Page:
    """Page 2: Task input form capturing prompt, course category, and priority."""
    content: list = [
        Header("Step 1: Describe Your Assignment or Question"),
        "Tip: Leave Course Category on 'General / Intro Electives' for broad "
        "tasks, or include course terms (like 'xlookup', 'dosage', 'organoid', "
        "'stoichiometry', or 'determinant') to trigger a +8 Keyword Clue Bonus.",
        HorizontalRule(),
    ]

    if error_message != "":
        content.append(Div(bold("Notice: "), error_message))

    content.append(bold("Assignment Prompt or Question:"))
    content.append(TextArea("prompt", state.user_prompt))
    content.append(LineBreak())
    content.append(bold("Course / Major Category (10 Tracks):"))
    content.append(SelectBox("category", CATEGORIES, state.selected_category))
    content.append(LineBreak())
    content.append(bold("Primary Priority:"))
    content.append(SelectBox("priority", PRIORITIES, state.selected_priority))
    content.append(HorizontalRule())
    content.append(Button("Find Top 5 Models", "recommend_model"))
    content.append(Button("View Scoring Rubric", "go_to_rubric"))
    content.append(Button("Back to Home", "index"))

    return Page(state, content)


def render_recommendation_page(state: State) -> Page:
    """Page 3: Displays the #1 winner, math breakdown, and Top 5 table."""
    top_five_models: list[ModelProfile] = get_top_five_by_score(state.models)
    top_five_table: Table = build_top_five_table(top_five_models)

    return Page(
        state,
        [
            Header("Step 2: Recommended Model & Score Breakdown"),
            Div(bold("Your Prompt: "), state.user_prompt),
            Div(
                bold("Selected Track: "),
                state.selected_category,
                " | ",
                bold("Priority: "),
                state.selected_priority,
            ),
            Div(bold("Keyword Analysis: "), state.keyword_feedback),
            Div(bold("Complexity Analysis: "), state.complexity_feedback),
            HorizontalRule(),
            Header("#1 Top Match: " + state.recommended_model_name, 2),
            state.recommendation_reason,
            LineBreak(),
            bold("Why " + state.recommended_model_name + " Earned This Score:"),
            BulletedList(state.winner_math_steps),
            HorizontalRule(),
            Header("Top 5 Models (Ranked Highest to Lowest)", 3),
            top_five_table,
            HorizontalRule(),
            Button("Evaluate an AI Response", "go_to_evaluate"),
            Button("View Full Scoring Rubric", "go_to_rubric"),
            Button("Modify Task Inputs", "go_to_input"),
            Button("View Saved Reviews", "go_to_history"),
        ],
    )


def render_evaluate_page(state: State, error_message: str = "") -> Page:
    """Page 4: Audit form allowing users to rate and verify an AI response."""
    model_names: list[str] = get_all_model_names(state.models)
    default_model: str = model_names[0]
    if state.recommended_model_name != "":
        default_model = state.recommended_model_name

    content: list = [
        Header("Step 3: Audit & Rate an AI Response"),
        "Test the recommended model on your assignment, then log accuracy, "
        "clarity, and fact-checking status to assign a trust verdict.",
        HorizontalRule(),
    ]

    if error_message != "":
        content.append(Div(bold("Notice: "), error_message))

    content.append(bold("Model Tested:"))
    content.append(SelectBox("model_name", model_names, default_model))
    content.append(LineBreak())
    content.append(bold("Course Track:"))
    content.append(SelectBox("category", CATEGORIES, state.selected_category))
    content.append(LineBreak())
    content.append(bold("Prompt Tested:"))
    content.append(TextArea("prompt_tested", state.user_prompt))
    content.append(LineBreak())
    content.append(bold("AI Response Snippet or Key Output:"))
    content.append(TextArea("response_snippet", ""))
    content.append(LineBreak())
    content.append(bold("Factual Accuracy Rating (1 = Poor, 5 = Verified Exact):"))
    content.append(SelectBox("accuracy_score", RATINGS, "4"))
    content.append(LineBreak())
    content.append(bold("Explanation Clarity Rating (1 = Confusing, 5 = Crystal Clear):"))
    content.append(SelectBox("clarity_score", RATINGS, "4"))
    content.append(LineBreak())
    content.append(CheckBox("fact_checked", False))
    content.append(" I fact-checked the answer against notes, textbooks, or code execution.")
    content.append(HorizontalRule())
    content.append(Button("Save Quality Evaluation", "submit_evaluation"))
    content.append(Button("View Saved Evaluations", "go_to_history"))
    content.append(Button("Back to Task Input", "go_to_input"))

    return Page(state, content)


def render_rubric_page(state: State) -> Page:
    """Page 5: Explains the scoring rubric, trust tiers, and all 20 models."""
    scoring_rules: list[str] = [
        "Track Alignment: +15 pts if the model specializes in your selected track; +5 pts for cross-domain support.",
        "Keyword Clue Bonus (+8 pts): Triggered when your prompt contains specialized course vocabulary matching a model's track.",
        "Complexity Bonus (+5 pts): Awarded to models with Accuracy >= 9 when prompts are 20+ words or contain advanced keywords.",
        "Priority Weighting (Highest Accuracy): Adds Accuracy Rating x 3 (up to +30 pts).",
        "Priority Weighting (Fastest Speed): Adds Speed Rating x 3 (up to +30 pts).",
        "Priority Weighting (Lowest Cost / Free): Adds +25 pts + Accuracy Rating for Free/Open models; subtracts -10 pts for Paid Tier models.",
    ]

    trust_rules: list[str] = [
        "High Trust (Verified): Accuracy >= 4/5, Clarity >= 4/5, and Fact-Checked box selected.",
        "Moderate Trust (Double-Check Details): Accuracy >= 3/5 and Clarity >= 3/5 (or unverified high rating).",
        "Low Trust (Needs Revision): Either Accuracy < 3/5 or Clarity < 3/5.",
    ]

    baseline_table: Table = build_baseline_models_table(state.models)

    return Page(
        state,
        [
            Header("Scoring & Answer Trust Rubric"),
            "Every recommendation is calculated deterministically from baseline "
            "benchmarks and prompt signals - no black-box rankings.",
            LineBreak(),
            Div(
                bold("Disclaimer: "),
                "Model ratings and access information are predefined estimates "
                "used for this educational comparison. Rankings are calculated "
                "using the application's scoring formula and are not live "
                "benchmark results. Model capabilities, availability, and "
                "pricing may change. Always verify important information with "
                "the provider.",
            ),
            HorizontalRule(),
            Header("1. Model Selection Point Formula", 2),
            BulletedList(scoring_rules),
            Header("2. Answer Quality Trust Verdicts", 2),
            BulletedList(trust_rules),
            HorizontalRule(),
            Header("3. Baseline Ratings for All 20 Models", 2),
            baseline_table,
            HorizontalRule(),
            Button("Start Model Selection", "go_to_input"),
            Button("Evaluate an AI Response", "go_to_evaluate"),
            Button("Back to Home", "index"),
        ],
    )


def render_history_page(state: State) -> Page:
    """Page 6: Displays saved response audits and the top-recommended leaderboard."""
    top_recommended: list[ModelProfile] = get_top_five_by_recommendations(state.models)
    leaderboard_table: Table = build_leaderboard_table(top_recommended)

    content: list = [
        Header("Saved Quality Evaluations & Model Leaderboard"),
        Header("Most Frequently Recommended Models (Session Leaderboard)", 2),
    ]

    if len(top_recommended) == 0:
        content.append(
            "No recommendations recorded yet. Run the model router "
            "to begin building the leaderboard."
        )
    else:
        content.append(leaderboard_table)

    content.append(HorizontalRule())
    content.append(
        Header("Logged Answer Quality Audits (" + str(len(state.evaluations)) + ")", 2)
    )

    if len(state.evaluations) == 0:
        content.append(
            "No evaluations logged yet. Run a model recommendation and click "
            "'Evaluate an AI Response' to audit an output."
        )
    else:
        content.append(build_evaluations_table(state.evaluations))

    content.append(HorizontalRule())
    content.append(Button("New Model Selection", "go_to_input"))
    content.append(Button("Log Another Evaluation", "go_to_evaluate"))
    if len(state.evaluations) > 0:
        content.append(Button("Clear Saved Evaluations", "clear_evaluations"))
    content.append(Button("Back to Home", "index"))

    return Page(state, content)


# ==============================================================================
# ROUTE HANDLERS
# ==============================================================================

@route
def index(state: State) -> Page:
    """Navigates to the home landing page."""
    return render_home_page(state)


@route
def go_to_input(state: State) -> Page:
    """Navigates to the task input form."""
    return render_input_page(state)


@route
def go_to_rubric(state: State) -> Page:
    """Navigates to the scoring rubric and model reference page."""
    return render_rubric_page(state)


@route
def go_to_history(state: State) -> Page:
    """Navigates to the saved evaluations and leaderboard page."""
    return render_history_page(state)


@route
def go_to_evaluate(state: State) -> Page:
    """Navigates to the response quality audit page."""
    return render_evaluate_page(state)


@route
def recommend_model(
    state: State, prompt: str, category: str, priority: str
) -> Page:
    """Scores all 20 models against the user's task and displays the Top 5."""
    cleaned_prompt: str = prompt.strip()
    if cleaned_prompt == "":
        return render_input_page(
            state,
            "Please enter an assignment prompt or question before running the router.",
        )

    state.user_prompt = cleaned_prompt
    state.selected_category = category
    state.selected_priority = priority

    keyword_category: str = find_keyword_category(cleaned_prompt)
    matched_keyword: str = find_matched_keyword(cleaned_prompt)
    if keyword_category != "":
        state.keyword_feedback = (
            "Detected term '"
            + matched_keyword
            + "' -> +8 Keyword Clue Bonus for "
            + keyword_category
            + " models."
        )
    else:
        state.keyword_feedback = (
            "No specialized track keyword detected (using selected category and priority)."
        )

    complex_task: bool = is_complex_prompt(cleaned_prompt)
    state.complexity_feedback = describe_prompt_complexity(cleaned_prompt)

    for model in state.models:
        model.last_score = calculate_model_score(
            model, category, priority, complex_task, keyword_category
        )
        model.bonus_summary = summarize_model_bonuses(
            model, complex_task, keyword_category
        )

    top_five: list[ModelProfile] = get_top_five_by_score(state.models)
    winner: ModelProfile = top_five[0]
    winner.times_recommended = winner.times_recommended + 1

    state.recommended_model_name = winner.name
    state.recommendation_reason = build_explanation(winner, category, priority)
    state.winner_math_steps = explain_model_score(
        winner, category, priority, complex_task, keyword_category
    )

    return render_recommendation_page(state)


@route
def submit_evaluation(
    state: State,
    model_name: str,
    category: str,
    prompt_tested: str,
    response_snippet: str,
    accuracy_score: str,
    clarity_score: str,
    fact_checked: bool,
) -> Page:
    """Validates and saves a user's AI response evaluation record."""
    cleaned_prompt: str = prompt_tested.strip()
    cleaned_snippet: str = response_snippet.strip()

    if cleaned_prompt == "" or cleaned_snippet == "":
        return render_evaluate_page(
            state,
            "Please fill in both the prompt tested and the AI response snippet.",
        )

    acc_int: int = int(accuracy_score)
    clar_int: int = int(clarity_score)
    verdict: str = determine_trust_verdict(acc_int, clar_int, fact_checked)

    record: EvaluationRecord = EvaluationRecord(
        model_name=model_name,
        category=category,
        prompt_tested=cleaned_prompt,
        response_snippet=cleaned_snippet,
        accuracy_score=acc_int,
        clarity_score=clar_int,
        fact_checked=fact_checked,
        trust_label=verdict,
    )
    state.evaluations.append(record)

    return render_history_page(state)


@route
def clear_evaluations(state: State) -> Page:
    """Clears all saved evaluation records from session state."""
    state.evaluations = []
    return render_history_page(state)


# Replace the placeholder strings below with your exact course example values
set_site_information(
    author="Gayathri Annapurna",
    description="College AI Model Router & Answer Quality Evaluator",
    sources=["Preset model ratings created for CISC106 final project"],
    planning="planning.pdf",
    links=["https://github.com/gayathri-annapurna/AI-Picker"],
)

start_server(create_initial_state())
