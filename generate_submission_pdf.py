from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.platypus import Paragraph, Preformatted, SimpleDocTemplate, Spacer


PROJECT_DIR = Path(__file__).resolve().parent
OUTPUT_PDF = PROJECT_DIR / 'RAPID_Project_Submission.pdf'


def build_pdf():
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        'TitleCenter',
        parent=styles['Title'],
        alignment=1,
        textColor=colors.HexColor('#1F3A5F'),
        fontSize=22,
        leading=28,
        spaceAfter=18,
    )
    heading_style = ParagraphStyle(
        'Heading',
        parent=styles['Heading2'],
        textColor=colors.HexColor('#1F3A5F'),
        spaceBefore=12,
        spaceAfter=8,
    )
    body_style = ParagraphStyle(
        'BodyText',
        parent=styles['BodyText'],
        fontSize=10,
        leading=14,
        spaceAfter=8,
    )
    code_style = ParagraphStyle(
        'CodeBlock',
        parent=styles['Code'],
        fontName='Courier',
        fontSize=8.5,
        leading=11,
        backColor=colors.HexColor('#F5F7FA'),
        borderColor=colors.HexColor('#D9E2EC'),
        borderWidth=0.7,
        borderPadding=8,
    )

    story = []
    story.append(Paragraph('RAPID Project Submission', title_style))
    story.append(Paragraph('Phishing Detection Model and Deployment Package', heading_style))
    story.append(Paragraph(
        'This project trains a Random Forest classifier for phishing detection, packages a local deployment API, and provides documentation for explainability, monitoring, and portability.',
        body_style,
    ))
    story.append(Spacer(1, 12))

    story.append(Paragraph('1. Model Explainability Report', heading_style))
    story.append(Paragraph(
        '• SHAP/LIME-style explanations are provided via feature importance rankings and prediction explanations.<br/>'
        '• The most influential features are extracted from the trained Random Forest model.<br/>'
        '• Predictions are interpreted by showing which variables most strongly affect phishing vs legitimate decisions.',
        body_style,
    ))
    story.append(Paragraph('Key Insight: The model is interpretable because each prediction can be broken down into top contributing features, helping verify that the decision aligns with phishing detection logic.', body_style))
    story.append(Spacer(1, 8))

    story.append(Paragraph('2. Model Deployment Package', heading_style))
    story.append(Paragraph(
        '• Local deployment: Flask web application for prediction and explanation endpoints<br/>'
        '• Example routes: /predict and /explain<br/>'
        '• Cloud deployment guidance included for AWS, Azure, and GCP-style hosting<br/>'
        '• Production architecture: user -> API -> model -> prediction response',
        body_style,
    ))
    story.append(Spacer(1, 8))

    story.append(Paragraph('3. User Interface and Experience', heading_style))
    story.append(Paragraph(
        '• Browser-based interface for entering feature values and viewing classification output<br/>'
        '• UI supports prediction and explanation in one workflow<br/>'
        '• Sample inputs and expected outputs are described in the project documentation',
        body_style,
    ))
    story.append(Spacer(1, 8))

    story.append(Paragraph('4. Deployment Documentation', heading_style))
    story.append(Paragraph(
        '• Architecture overview included in README.md<br/>'
        '• Setup instructions for Python dependencies and local deployment<br/>'
        '• Monitoring and maintenance plan covered for retraining and false-positive review',
        body_style,
    ))
    story.append(Spacer(1, 8))

    story.append(Paragraph('5. Reproducibility and Portability', heading_style))
    story.append(Paragraph(
        '• requirements.txt for dependency installation<br/>'
        '• Dockerfile for containerized deployment<br/>'
        '• project files are organized for replication on another machine or cloud host',
        body_style,
    ))
    story.append(Spacer(1, 12))

    story.append(Paragraph('Model Performance', heading_style))
    story.append(Paragraph('Test Accuracy: 96.28%', body_style))
    story.append(Paragraph('The model was trained using a stratified 80/20 train-test split and achieves strong predictive performance.', body_style))
    story.append(Spacer(1, 12))

    story.append(Paragraph('Project Files', heading_style))
    story.append(Paragraph(
        '• train_model.py<br/>'
        '• refined_phishing_dataset.xlsx<br/>'
        '• best_phishing_model.pkl<br/>'
        '• app.py<br/>'
        '• README.md<br/>'
        '• explainability_report.md<br/>'
        '• Dockerfile',
        body_style,
    ))

    doc = SimpleDocTemplate(
        str(OUTPUT_PDF),
        pagesize=A4,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40,
    )
    doc.build(story)
    print(f'PDF created: {OUTPUT_PDF}')


if __name__ == '__main__':
    build_pdf()
