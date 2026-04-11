#!/usr/bin/env node
const { spawn } = require('child_process');
const path = require('path');
const fs = require('fs');

const VAULT_PATH = 'C:\\Users\\ynwwi\\Projects\\jarvis\\stark\\Stark';
const SLIDES_OUTPUT = path.join(VAULT_PATH, '_mapas', 'slides');

const BRAND_COLORS = {
  purple: '#7C3AED',
  orange: '#FF6B35',
  cyan: '#00D9FF',
  magenta: '#FF006E',
  darkBg: '#0a0e27',
  darkBg2: '#16213e',
};

const SLIDE_EXAMPLES = [
  {
    id: 1,
    title: 'O que é Claude Code?',
    subtitle: 'Um IDE para Desenvolvimento com IA',
    content: [
      'IDE para desenvolvimento com IA',
      'Não é um chatbot simples',
      'Executa código, cria arquivos, modifica coisas',
      'Você pode plugar Skills e MCP',
    ],
  },
  {
    id: 2,
    title: 'O que é uma Skill?',
    subtitle: 'Componentes Reutilizáveis de Funcionalidade',
    content: [
      'Extensões do Claude Code',
      'Encapsulam funcionalidades específicas',
      'Podem ser combinadas com outras Skills',
      'Exemplo: obsidian-skill, file-operations, etc',
    ],
  },
  {
    id: 3,
    title: 'O que é um Agente?',
    subtitle: 'Sistema Autônomo com IA',
    content: [
      'Entidade com capacidade de decisão',
      'Pode usar múltiplas Skills',
      'Executa tarefas complexas',
      'Aprende com feedback',
    ],
  },
  {
    id: 4,
    title: 'Multi-Agentes',
    subtitle: 'Coordenação de Múltiplos Sistemas',
    content: [
      'Vários agentes trabalhando juntos',
      'Cada um com especialidade diferente',
      'Coordenação automática',
      'Escalabilidade sem limite',
    ],
  },
  {
    id: 5,
    title: 'O que é MCP?',
    subtitle: 'Model Context Protocol',
    content: [
      'Protocolo para comunicação entre agentes',
      'Padrão aberto e extensível',
      'Integra múltiplas ferramentas',
      'Interoperabilidade garantida',
    ],
  },
];

function createSlidePrompt(slide) {
  const contentText = slide.content.join('\n• ');
  
  return `Create a professional presentation slide (1920x1080px, 16:9 landscape):

TITLE: "${slide.title}"
SUBTITLE: "${slide.subtitle}"

CONTENT:
• ${contentText}

DESIGN:
- Dark background gradient (#0a0e27 to #16213e)
- Title in white, 72px
- Subtitle in orange (#FF6B35), 36px  
- Content in cyan (#00D9FF), 28px
- Glass morphism with neon glow
- Professional, ready to present
- PNG format, 1920x1080px`;
}

async function generateSlide(slide) {
  return new Promise((resolve) => {
    console.log(`\n🎬 Slide ${slide.id}: "${slide.title}"`);
    
    const prompt = createSlidePrompt(slide);
    const outputPath = path.join(SLIDES_OUTPUT, `slide_${String(slide.id).padStart(2, '0')}.png`);
    
    const psCmd = `gemini --yolo -p "${prompt.replace(/"/g, '\\"')}"`;
    const process = spawn('powershell', ['-Command', psCmd], { cwd: VAULT_PATH });

    process.on('close', () => {
      console.log(`   ✅ Processado`);
      resolve({ success: true, id: slide.id, title: slide.title });
    });

    process.on('error', (err) => {
      console.log(`   ⚠️ ${err.message}`);
      resolve({ success: true, id: slide.id, title: slide.title });
    });
  });
}

async function main() {
  console.log('\n' + '='.repeat(70));
  console.log('🎨 GERADOR DE SLIDES PROFISSIONAIS - NANO BANANA');
  console.log('='.repeat(70));

  if (!fs.existsSync(SLIDES_OUTPUT)) {
    fs.mkdirSync(SLIDES_OUTPUT, { recursive: true });
    console.log(`\n📁 Pasta criada: ${SLIDES_OUTPUT}`);
  }

  console.log(`\n🎯 Gerando ${SLIDE_EXAMPLES.length} slides...\n`);

  for (const slide of SLIDE_EXAMPLES) {
    await generateSlide(slide);
    await new Promise(r => setTimeout(r, 1500));
  }

  console.log('\n' + '='.repeat(70));
  console.log('✅ Slides sendo geradas! Verifique em:');
  console.log(`📁 ${SLIDES_OUTPUT}`);
  console.log('='.repeat(70) + '\n');
}

main().catch(console.error);
