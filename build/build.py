# -*- coding: utf-8 -*-
"""Gera todas as páginas do site do Instituto Correr."""
import os, sys, json
try:
    sys.stdout.reconfigure(encoding="utf-8")
except AttributeError:
    pass
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from partials import *
import schema as S

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")


def write(name, html):
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        f.write(html)
    print("  ✓", name, "(%.1f KB)" % (len(html.encode()) / 1024))


def cards_tratamentos(limit=None, show_bullets=True):
    out = ""
    for i, t in enumerate(TREATMENTS[:limit] if limit else TREATMENTS):
        b = ""
        if show_bullets:
            b = "<ul>" + "".join("<li>" + x + "</li>" for x in t["bullets"]) + "</ul>"
        wmsg = wa_link("Olá! Gostaria de agendar uma avaliação de " + t["nome"] + " no Instituto Correr.")
        out += ('<article class="card tcard reveal" data-d="' + str(i % 4) + '">'
                '<span class="ic">' + IC[t["icon"]] + '</span>'
                '<h3>' + t["nome"] + '</h3>'
                '<p>' + t["curto"] + '</p>' + b +
                '<div class="tcard__foot">'
                '<a class="btn btn--wa btn--sm" href="' + wmsg + '" target="_blank" rel="noopener">' + IC["whatsapp"] + ' Agendar</a>'
                '<a class="tlink" href="' + t["slug"] + '.html">Detalhes ' + IC["arrow"] + '</a>'
                '</div>'
                '</article>')
    return out


def cards_svc(limit=None):
    """Cards de serviço centralizados, brancos, para usar sobre a faixa verde."""
    out = ""
    for i, t in enumerate(TREATMENTS[:limit] if limit else TREATMENTS):
        wmsg = wa_link("Olá! Gostaria de agendar uma avaliação de " + t["nome"] + " no Instituto Correr.")
        out += ('<article class="svc reveal" data-d="' + str(i % 4) + '">'
                '<span class="ic">' + IC[t["icon"]] + '</span>'
                '<h3>' + t["nome"] + '</h3>'
                '<p>' + t["curto"] + '</p>'
                '<div class="svc__actions">'
                '<a class="btn btn--wa btn--sm" href="' + wmsg + '" target="_blank" rel="noopener">' + IC["whatsapp"] + ' Agendar</a>'
                '<a class="btn btn--ghost btn--sm" href="' + t["slug"] + '.html">Saiba mais</a>'
                '</div>'
                '</article>')
    return out


TEAM = [
    dict(img="roger", nome="Roger Levi Andrade", role="Fisioterapeuta · Responsável Técnico",
         reg="CREFITO 175512",
         bio="Fundador e gestor do Instituto. Dez anos de prática clínica com foco em prevenção, reabilitação e performance esportiva, com especialização em acupuntura e técnicas manuais."),
    dict(img="carla", nome="Carla Morgana Pintarelli", role="Fisioterapeuta", reg="Formada pela FURB",
         bio="Formada desde 2012, atua com o Método Busquet, treinamento funcional e pilates. Trabalha a integração entre corpo e mente em cada plano de tratamento."),
    dict(img="ketlin", nome="Ketlin Cardoso", role="Financeiro e Agendamentos", reg="Experiência em estética",
         bio="Cuida da agenda, do financeiro e da experiência de quem chega ao Instituto, do primeiro contato ao acompanhamento do plano."),
    dict(img="terezinha", nome="Terezinha", role="Recepção", reg="",
         bio="O primeiro rosto de quem chega pela manhã. Recebe cada paciente pelo nome e mantém o clima leve que define a casa."),
]


def cards_equipe(bio=True):
    out = ""
    for i, m in enumerate(TEAM):
        reg = m["reg"].strip()
        out += ('<article class="team-card reveal" data-d="' + str(i % 4) + '">'
                '<div class="team-card__media">'
                '<img src="assets/img/' + m["img"] + '.webp" alt="' + m["nome"] + ', ' + m["role"]
                + ' do Instituto Correr" width="384" height="538" loading="lazy">'
                '<div class="team-card__over">'
                '<h3>' + m["nome"] + '</h3>'
                '<span class="role">' + m["role"] + '</span>'
                + ('<span class="reg">' + reg + '</span>' if reg else '') +
                '</div>'
                '</div>'
                + ('<p class="team-card__bio">' + m["bio"] + '</p>' if bio else '') +
                '</article>')
    return out


def symptom_cards(items, service_label=""):
    """Gera grade de queixas clicáveis que abrem o WhatsApp já com a queixa preenchida."""
    out = '<div class="qgrid mt-8">'
    prefix = ("Olá! Gostaria de agendar uma avaliação de " + service_label + " no Instituto Correr. "
              if service_label else "Olá! Gostaria de agendar uma avaliação no Instituto Correr. ")
    for i, (titulo, sub) in enumerate(items):
        wh = wa_link(prefix + "Minha principal queixa é: " + titulo + ".")
        out += ('<a class="qcard reveal" data-d="' + str(i % 3) + '" href="' + wh
                + '" target="_blank" rel="noopener" data-track-loc="triagem_queixa">'
                '<div class="qcard__txt"><b>' + titulo + '</b><span>' + sub + '</span></div>'
                '<span class="qcard__cta">' + IC["whatsapp"] + '<span>Falar</span></span>'
                '</a>')
    out += '</div>'
    return out


# ==========================================================================
# HOME
# ==========================================================================
QUEIXAS_HOME = [
    ("Dor na coluna (lombar ou cervical)", "Travamento, queimação ou dor ao sentar e levantar"),
    ("Hérnia de disco e nervo ciático", "Dor irradiada para perna, glúteo ou braço"),
    ("Dor no ombro, joelho ou quadril", "Limitação ao caminhar, subir escada ou treinar"),
    ("Lesões no esporte e na corrida", "Recuperação e retorno seguro aos treinos"),
    ("Pós-operatório ortopédico", "Reabilitação guiada etapa por etapa"),
    ("Dor de cabeça e tensão no pescoço", "Cefaleia cervical, estalos e sobrecarga postural"),
]

FAQ_HOME = [
 ("Preciso de pedido médico para fazer fisioterapia?",
  "Não. O fisioterapeuta é um profissional de primeiro contato: você pode agendar sua avaliação diretamente conosco. Se durante a avaliação identificarmos a necessidade de exames ou de acompanhamento médico, orientamos e encaminhamos."),
 ("Como funciona a primeira consulta?",
  "A primeira sessão é uma avaliação detalhada: conversa sobre sua história e sua queixa, exame físico e funcional, testes de movimento e, quando necessário, recursos de tecnologia para medir o que os olhos não veem. Você sai dela entendendo o que está acontecendo e com um plano definido."),
 ("Quantas sessões vou precisar?",
  "Depende do que a avaliação encontrar. Não trabalhamos com pacotes fechados vendidos antes de examinar você. O número de sessões é uma consequência do diagnóstico funcional, e é revisado ao longo do tratamento conforme sua resposta."),
 ("Vocês atendem convênios?",
  "Trabalhamos com atendimento particular e emitimos recibo para reembolso junto ao seu plano de saúde. Consulte as condições do seu convênio e fale com a gente pelo WhatsApp para tirar dúvidas sobre valores e formas de pagamento."),
 ("O tratamento dói?",
  "Executar corretamente um movimento não precisa ser sofrido. Algumas técnicas manuais geram desconforto momentâneo em pontos de tensão, mas dosagem e intensidade são ajustadas a você. Dor não é sinal de que o tratamento está funcionando."),
 ("Faço exercício e sinto dor. Devo parar?",
  "Nem sempre. A dor é um sinal de proteção e precisa ser interpretada, não silenciada. Na avaliação identificamos o que está gerando o alerta e ajustamos carga, técnica e volume. O objetivo é você continuar se movendo com segurança, e não parar."),
]


def build_home():
    sch = S.tags(S.ORG, S.ROGER, S.CARLA, S.WEBSITE, S.faq(FAQ_HOME))
    h = head(
        "Fisioterapia e Quiropraxia em Blumenau | Instituto Correr",
        "Fisioterapia, quiropraxia e pilates em Blumenau/SC. Avaliação detalhada e tratamento individualizado para você voltar a se mover sem dor.",
        SITE + "/", sch, preload="assets/img/hero.jpg", page_img="hero.jpg")
    h += header("index.html", overlay=True)
    h += """
<main id="main">

<!-- ===== HERO ===== -->
<section class="hero hero--full">
  <div class="hero__bg">
    <img src="assets/img/hero.jpg" alt="Pessoa correndo ao ar livre, retomando as atividades sem dor" width="1920" height="1047" fetchpriority="high">
  </div>
  <div class="container hero__inner">
    <div class="hero__copy">
      <span class="eyebrow reveal">Fisioterapia, quiropraxia e pilates em Blumenau</span>
      <h1 class="reveal" data-d="1">Volte a fazer o que quiser, <em>sem se preocupar com a dor</em></h1>
      <p class="lead reveal" data-d="2">Avaliação física detalhada e conduta individualizada em Blumenau. Tratamos a causa do problema, não só o sintoma, para você recuperar o movimento com segurança e sem recaída.</p>
      <div class="btn-row reveal" data-d="3">
        <a class="btn btn--wa btn--lg" href="@@WA@@" target="_blank" rel="noopener">@@ICWA@@ Agendar avaliação no WhatsApp</a>
        <a class="btn btn--light btn--lg" href="#queixas">Escolher minha queixa</a>
      </div>
      <p class="thero__micro reveal" data-d="3">@@ICCLK@@ Centro/Garcia, Blumenau · Seg. a sex. até as 20h · Sem pedido médico</p>
    </div>
    <div class="hero__foot reveal" data-d="4">
      <div class="hero__badge">
        <span class="ic">@@ICSHIELD@@</span>
        <div><b>Avaliação antes de qualquer conduta</b><span>CREFITO 175512 · Particular c/ recibo p/ reembolso</span></div>
      </div>
      <div class="statpills">
        <div class="statpill"><b><span data-count="10">0</span>+</b><span>anos de prática clínica</span></div>
        <div class="statpill"><b><span data-count="5">0</span></b><span>especialidades integradas</span></div>
        <div class="statpill"><b>20h</b><span>atendimento seg. a sex.</span></div>
      </div>
    </div>
  </div>
</section>

<!-- ===== TRIAGEM INTERATIVA DE QUEIXAS ===== -->
<section class="section section--tight section--soft" id="queixas">
  <div class="container">
    <div class="sec-head sec-head--center">
      <span class="eyebrow eyebrow--center reveal">Atendimento direto</span>
      <h2 class="reveal" data-d="1">O que está incomodando você hoje?</h2>
      <p class="reveal" data-d="2">Toque na opção mais próxima do seu caso para abrir o WhatsApp já com a mensagem preenchida para a nossa equipe.</p>
    </div>
    @@QHOME@@
  </div>
</section>

<!-- ===== VÍDEO EM DESTAQUE ===== -->
<section class="section section--sand">
  <div class="container container--narrow">
    <div class="sec-head sec-head--center">
      <span class="eyebrow eyebrow--center reveal">Em vídeo</span>
      <h2 class="reveal" data-d="1">Conheça o Instituto por dentro</h2>
      <p class="reveal" data-d="2">Uma volta pela estrutura e pelo clima do atendimento em Blumenau.</p>
    </div>
    <div class="mt-8">@@VIDEO@@</div>
  </div>
</section>

<!-- ===== PROBLEMA / DIFERENCIAL ===== -->
<section class="section">
  <div class="container">
    <div class="split">
      <div class="reveal">
        <div class="media-img media-img--plain"><img src="assets/img/metodo.webp" alt="Fisioterapeuta do Instituto Correr avaliando o movimento de um paciente" width="800" height="757" loading="lazy"></div>
      </div>
      <div>
        <span class="eyebrow reveal">Por que aqui é diferente</span>
        <h2 class="reveal mt-5" data-d="1">Conviver com a dor não deveria ser a sua rotina</h2>
        <p class="lead reveal mt-5" data-d="1">Muita gente passa anos alternando entre alívio momentâneo e o retorno da mesma dor. Isso acontece quando o tratamento persegue o sintoma e ignora o que o produziu.</p>
        <p class="reveal mt-5" data-d="2">Personalização no atendimento é saber exatamente <strong>o que pede cada dor</strong> e <strong>quais ferramentas</strong> podem ser utilizadas. Por isso começamos sempre pela avaliação, e só depois definimos a conduta.</p>
        <ul class="rulelist reveal mt-6" data-d="3">
          <li><span class="n">01</span> Avaliação detalhada antes de qualquer técnica</li>
          <li><span class="n">02</span> Equipe multidisciplinar com formação continuada</li>
          <li><span class="n">03</span> Tecnologia aplicada com critério clínico</li>
        </ul>
        <div class="btn-row reveal mt-6" data-d="3">
          <a class="btn btn--wa" href="@@WA@@" target="_blank" rel="noopener">@@ICWA@@ Conversar sobre o meu caso</a>
          <a class="btn btn--ghost" href="sobre.html">Conhecer o Instituto</a>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ===== TRATAMENTOS (faixa verde) ===== -->
<section class="section section--dark" id="tratamentos">
  <div class="container">
    <div class="sec-head sec-head--center">
      <span class="eyebrow eyebrow--center reveal">Tratamentos</span>
      <h2 class="reveal" data-d="1">Cinco especialidades, um só raciocínio clínico</h2>
      <p class="reveal" data-d="2">Não escolhemos a técnica antes de entender o problema. A avaliação define qual combinação de recursos resolve o seu caso no menor tempo possível.</p>
    </div>
    <div class="svc-grid mt-8">@@SVC@@</div>
    <div class="center mt-8">
      <a class="btn btn--light reveal" href="tratamentos.html">Comparar todos os tratamentos</a>
    </div>
  </div>
</section>

<!-- ===== JORNADA ===== -->
<section class="section">
  <div class="container">
    <div class="split split--top">
      <div class="sticky-col">
        <span class="eyebrow reveal">Como funciona</span>
        <h2 class="reveal mt-5" data-d="1">Da primeira conversa até a alta</h2>
        <p class="lead reveal mt-5" data-d="2">Um caminho claro, com objetivos definidos em cada etapa. Você sempre sabe onde está e o que vem a seguir.</p>
        <div class="btn-row reveal mt-6" data-d="3">
          <a class="btn btn--wa" href="@@WA@@" target="_blank" rel="noopener">@@ICWA@@ Começar pela avaliação</a>
        </div>
      </div>
      <div class="steps reveal">
        <div class="step"><div class="step__n">1</div><div><h3>Contato e agendamento</h3><p>Você fala com a gente pelo WhatsApp ou telefone, conta rapidamente o que está sentindo e escolhe o melhor horário. Agenda com disponibilidade rápida.</p></div></div>
        <div class="step"><div class="step__n">2</div><div><h3>Avaliação detalhada</h3><p>Conversa sobre sua história, exame físico e funcional, testes de movimento e, quando indicado, recursos tecnológicos. É aqui que o diagnóstico funcional aparece.</p></div></div>
        <div class="step"><div class="step__n">3</div><div><h3>Plano individualizado</h3><p>Definimos objetivos, quais técnicas serão usadas, com que frequência e em quanto tempo esperamos cada marco. Você entende e concorda com o plano antes de começar.</p></div></div>
        <div class="step"><div class="step__n">4</div><div><h3>Tratamento e reavaliação</h3><p>Sessões conduzidas por especialistas, com reavaliação periódica. Se o corpo responde diferente do esperado, o plano muda, e não você que se adapta ao protocolo.</p></div></div>
        <div class="step"><div class="step__n">5</div><div><h3>Alta e manutenção</h3><p>Recuperação completa, sem recidivas. Você sai com orientação de manutenção e, se quiser, segue no pilates para não voltar ao ponto de partida.</p></div></div>
      </div>
    </div>
  </div>
</section>

<!-- ===== EQUIPE ===== -->
<section class="section section--mute">
  <div class="container">
    <div class="sec-head sec-head--center">
      <span class="eyebrow eyebrow--center reveal">Quem cuida de você</span>
      <h2 class="reveal" data-d="1">Uma equipe multidisciplinar com olhar humano</h2>
      <p class="reveal" data-d="2">Fisioterapeutas, quiropraxia e uma estrutura de atendimento pensada para que você se sinta acolhido do primeiro contato à alta.</p>
    </div>
    <div class="grid grid-4 mt-8">@@TEAM@@</div>
    <div class="center mt-8"><a class="btn btn--ghost reveal" href="equipe.html">Conhecer a equipe</a></div>
  </div>
</section>

<!-- ===== DEPOIMENTOS =====
     ⚠️  ATENÇÃO: os depoimentos abaixo são EXEMPLOS de layout.
     Substitua por avaliações reais (Google Meu Negócio / pacientes com autorização)
     antes de publicar o site. -->
<section class="section section--soft">
  <div class="container">
    <div class="sec-head sec-head--center">
      <span class="eyebrow eyebrow--center reveal">Depoimentos</span>
      <h2 class="reveal" data-d="1">Histórias de quem voltou a se mover</h2>
    </div>
    <div class="grid grid-3 mt-8">
      <article class="tstm reveal">
        <div class="stars" aria-label="5 de 5 estrelas">@@ST5@@</div>
        <blockquote>Cheguei com uma dor lombar que já durava mais de um ano e achando que ia ter que conviver com aquilo. A diferença aqui foi a avaliação: pela primeira vez alguém me explicou o porquê da dor. Voltei a correr em três meses.</blockquote>
        <footer><span class="av">M</span><div><b>Marcelo A.</b><small>Corredor amador · Blumenau</small></div></footer>
      </article>
      <article class="tstm reveal" data-d="1">
        <div class="stars" aria-label="5 de 5 estrelas">@@ST5@@</div>
        <blockquote>Fiz quiropraxia por causa de dores de cabeça constantes que nenhum remédio resolvia. O tratamento foi tranquilo e o acompanhamento, atencioso. Hoje as crises são raras e eu sei o que fazer quando aparecem.</blockquote>
        <footer><span class="av">J</span><div><b>Juliana R.</b><small>Paciente · Blumenau</small></div></footer>
      </article>
      <article class="tstm reveal" data-d="2">
        <div class="stars" aria-label="5 de 5 estrelas">@@ST5@@</div>
        <blockquote>Entrei no pilates depois da reabilitação do joelho e nunca mais parei. As séries são feitas para mim, não para a turma. É o único lugar onde eu sinto que estão prestando atenção no meu movimento.</blockquote>
        <footer><span class="av">P</span><div><b>Patrícia L.</b><small>Aluna do estúdio · Blumenau</small></div></footer>
      </article>
    </div>
  </div>
</section>

@@FASTHOME@@

<!-- ===== FAQ ===== -->
<section class="section">
  <div class="container">
    <div class="split split--faq">
      <div class="sticky-col">
        <span class="eyebrow reveal">Dúvidas frequentes</span>
        <h2 class="reveal mt-5" data-d="1">Antes de agendar, talvez você queira saber</h2>
        <p class="reveal mt-5" data-d="2">Não encontrou sua dúvida? Fale com a gente pelo WhatsApp. Respondemos rápido em horário comercial.</p>
        <div class="btn-row reveal mt-6" data-d="3">
          <a class="btn btn--wa" href="@@WA@@" target="_blank" rel="noopener">@@ICWA@@ Perguntar no WhatsApp</a>
        </div>
      </div>
      <div class="reveal">@@FAQ@@</div>
    </div>
  </div>
</section>

<!-- ===== LOCALIZAÇÃO ===== -->
<section class="section section--soft">
  <div class="container">
    <div class="split">
      <div>
        <span class="eyebrow reveal">Onde estamos</span>
        <h2 class="reveal mt-5" data-d="1">No centro de Blumenau, fácil de chegar</h2>
        <div class="grid mt-6" style="gap:1rem">
          <div class="infocard reveal" data-d="1"><span class="ic">@@ICMAP@@</span><div><h3>Endereço</h3><p>@@STREET@@<br>@@CITY@@/@@STATE@@, CEP @@CEP@@</p></div></div>
          <div class="infocard reveal" data-d="2"><span class="ic">@@ICCLK@@</span><div><h3>Horário</h3><p>@@HOURS@@</p></div></div>
          <div class="infocard reveal" data-d="3"><span class="ic">@@ICPH@@</span><div><h3>Telefone e WhatsApp</h3><a href="tel:@@TEL@@">@@PH@@</a></div></div>
        </div>
      </div>
      <div class="map-wrap reveal" data-d="1">
        <iframe title="Mapa do Instituto Correr, Blumenau/SC" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen
          src="https://www.google.com/maps?q=Rua%20Frederico%20Busch%20Junior%2C%20101%20-%20Blumenau%2C%20SC&output=embed"></iframe>
      </div>
    </div>
  </div>
</section>

</main>
""".replace("@@QHOME@@", symptom_cards(QUEIXAS_HOME)).replace("@@FASTHOME@@", fast_schedule_section(""))
    h += cta_band()
    h += footer()
    return _fill(h, svc=cards_svc(), team=cards_equipe(bio=False), faq=acc(FAQ_HOME))


# ==========================================================================
# helper de substituição global
# ==========================================================================
def _fill(h, tcards="", team="", faq="", svc=""):
    reps = {
        "@@WA@@": wa_link(), "@@ICWA@@": IC["whatsapp"], "@@ICARR@@": IC["arrow"],
        "@@ICCHK@@": IC["check"], "@@ICC@@": IC["check"], "@@ICSHIELD@@": IC["shield"],
        "@@ICMAP@@": IC["map"], "@@ICCLK@@": IC["clock"], "@@ICPH@@": IC["phone"],
        "@@ICMAIL@@": IC["mail"], "@@ICAWARD@@": IC["award"], "@@ICUSERS@@": IC["users"],
        "@@ICMICRO@@": IC["microscope"], "@@ICTARGET@@": IC["target"], "@@ICBRAIN@@": IC["brain"],
        "@@ICHEART@@": IC["heart"], "@@ICSPARK@@": IC["sparkles"], "@@ICREPEAT@@": IC["repeat"],
        "@@ICZAP@@": IC["zap"], "@@ICCAL@@": IC["calendar"], "@@ICFILE@@": IC["file"],
        "@@ICTREND@@": IC["trending"], "@@ICACT@@": IC["activity"],
        "@@ST5@@": IC["star"] * 5,
        "@@TEL@@": PHONE_TEL, "@@PH@@": PHONE_DISPLAY, "@@EMAIL@@": EMAIL, "@@EML@@": email_html(),
        "@@HOURS@@": HOURS, "@@STREET@@": STREET, "@@CITY@@": CITY,
        "@@STATE@@": STATE, "@@CEP@@": CEP,
        "@@TCARDS@@": tcards, "@@TEAM@@": team, "@@FAQ@@": faq, "@@SVC@@": svc,
        "@@VIDEO@@": video(),
    }
    for k, v in reps.items():
        h = h.replace(k, v)
    return h


# ==========================================================================
# SOBRE
# ==========================================================================
def build_sobre():
    sch = S.tags(S.ORG, S.ROGER, S.CARLA, S.WEBSITE, S.breadcrumb([("Sobre nós", "sobre.html")]))
    h = head("Sobre o Instituto Correr | Clínica de Fisioterapia em Blumenau",
             "Clínica de fisioterapia, quiropraxia e pilates em Blumenau/SC. Equipe multidisciplinar e base científica para prevenção, reabilitação e performance.",
             SITE + "/sobre.html", sch)
    h += header("sobre.html")
    h += phero([("Sobre nós", None)], "O Instituto",
               "Cuidar da saúde do seu movimento",
               "A gente te ajuda a manter a saúde dos seus movimentos e a respeitar o seu corpo pra você não se machucar.")
    h += """
<main id="main">

<section class="section">
  <div class="container">
    <div class="split">
      <div>
        <span class="eyebrow reveal">Nossa razão de existir</span>
        <h2 class="reveal mt-5" data-d="1">Movimento não precisa ser sofrimento</h2>
        <p class="lead reveal mt-5" data-d="1">Existe muito mito circulando sobre exercício: o que pode, o que não pode, o que estraga o joelho, o que detona a coluna. Boa parte do que trava as pessoas é informação errada.</p>
        <p class="reveal mt-5" data-d="2"><strong>Executar corretamente um movimento não é difícil e nem precisa ser sofrido.</strong> Quando você entende como o seu corpo funciona, o risco de lesão cai e a adesão ao exercício sobe, porque deixa de existir o medo de se machucar.</p>
        <p class="reveal mt-5" data-d="2">É esse o trabalho do Instituto Correr: desmistificar, orientar o movimento seguro e devolver a você uma relação positiva com o próprio corpo.</p>
        <div class="btn-row reveal mt-6" data-d="3">
          <a class="btn btn--wa" href="@@WA@@" target="_blank" rel="noopener">@@ICWA@@ Agendar avaliação no WhatsApp</a>
          <a class="btn btn--ghost" href="metodo.html">Ver o método</a>
        </div>
      </div>
      <div class="reveal" data-d="1">
        <div class="media-img media-img--plain"><img src="assets/img/metodo.webp" alt="Atendimento no Instituto Correr" width="768" height="727" loading="lazy"></div>
      </div>
    </div>
  </div>
</section>

<section class="section section--soft">
  <div class="container">
    <div class="sec-head sec-head--center">
      <span class="eyebrow eyebrow--center reveal">Três frentes de atuação</span>
      <h2 class="reveal" data-d="1">Prevenir, reabilitar e melhorar performance</h2>
      <p class="reveal" data-d="2">O Instituto atua nos três momentos da relação entre você e o movimento: antes que a lesão aconteça, durante a recuperação e quando o objetivo é ir além.</p>
    </div>
    <div class="grid grid-3 mt-8">
      <article class="card reveal"><span class="ic">@@ICSHIELD@@</span><h3>Prevenção</h3><p>Identificar padrões de sobrecarga, corrigir mecânica de movimento e ajustar carga antes que o corpo mande o aviso pela dor. É o trabalho mais barato e mais eficiente que existe.</p></article>
      <article class="card reveal" data-d="1"><span class="ic">@@ICHEART@@</span><h3>Reabilitação</h3><p>Recuperação de lesões, pós-operatório e quadros crônicos com um plano que persegue a causa. Objetivo: retorno breve e seguro às atividades cotidianas, com recuperação total e sem recidivas.</p></article>
      <article class="card reveal" data-d="2"><span class="ic">@@ICTREND@@</span><h3>Performance</h3><p>Para quem treina, compete ou simplesmente quer render mais: avaliação de movimento, correção de gestos esportivos e condicionamento voltado ao seu esporte.</p></article>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="sec-head">
      <span class="eyebrow reveal">Diferenciais</span>
      <h2 class="reveal" data-d="1">O que faz o atendimento aqui ser outro</h2>
    </div>
    <div class="grid grid-2 mt-8">
      <article class="card reveal"><span class="ic">@@ICUSERS@@</span><h3>Equipe multidisciplinar</h3><p>Fisioterapia, quiropraxia, pilates e terapias manuais sob o mesmo teto e conversando entre si. Você não precisa reexplicar a sua história a cada profissional, porque o caso é discutido internamente.</p></article>
      <article class="card reveal" data-d="1"><span class="ic">@@ICMICRO@@</span><h3>Método com base científica</h3><p>As condutas partem de evidência atual e de raciocínio clínico, não de modismo. E são revisadas conforme a sua resposta ao tratamento.</p></article>
      <article class="card reveal" data-d="2"><span class="ic">@@ICZAP@@</span><h3>Estrutura e tecnologia</h3><p>Estúdio de pilates completo, recursos de avaliação e tecnologia aplicada com critério, sempre a serviço do protocolo e nunca como espetáculo.</p></article>
      <article class="card reveal" data-d="3"><span class="ic">@@ICTARGET@@</span><h3>Olhar humano e integrado</h3><p>Você é uma pessoa com contexto, rotina, trabalho e limites, não um segmento corporal isolado. O plano precisa caber na sua vida para funcionar.</p></article>
    </div>
  </div>
</section>

<section class="section section--dark">
  <div class="container">
    <div class="quote reveal mx-auto" style="max-width:820px">
      <p>&ldquo;Personalização no atendimento é saber exatamente o que pede cada dor e quais ferramentas podem ser utilizadas.&rdquo;</p>
      <cite>Instituto Correr, Blumenau/SC</cite>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="sec-head sec-head--center">
      <span class="eyebrow eyebrow--center reveal">A equipe</span>
      <h2 class="reveal" data-d="1">Quem vai cuidar de você</h2>
    </div>
    <div class="grid grid-4 mt-8">@@TEAM@@</div>
    <div class="center mt-8"><a class="btn btn--ghost reveal" href="equipe.html">Ver perfis completos</a></div>
  </div>
</section>

</main>
"""
    h += cta_band()
    h += footer()
    return _fill(h, team=cards_equipe(bio=False))


# ==========================================================================
# MÉTODO
# ==========================================================================
FAQ_METODO = [
 ("A avaliação é cobrada separadamente?",
  "A avaliação é uma sessão em si: é nela que o diagnóstico funcional é construído e o plano definido. Fale com a recepção pelo WhatsApp para conhecer valores e formas de pagamento."),
 ("Quanto tempo dura cada sessão?",
  "Varia conforme a conduta definida na avaliação. Sessões de terapia manual e quiropraxia costumam ser mais curtas e objetivas; sessões de reabilitação com exercício e pilates são mais longas. O tempo é informado no seu plano."),
 ("Posso combinar mais de uma técnica?",
  "Sim, e é o mais comum. A avaliação frequentemente indica combinações, como terapia manual para reduzir a dor somada a exercício para resolver a causa e pilates para manutenção."),
 ("E se eu não estiver evoluindo como o esperado?",
  "A reavaliação existe justamente para isso. Se o corpo responde diferente do previsto, o plano é ajustado e, quando o caso pede outra especialidade, orientamos e encaminhamos."),
]


def build_metodo():
    sch = S.tags(S.ORG, S.ROGER, S.CARLA, S.WEBSITE, S.breadcrumb([("Nosso método", "metodo.html")]), S.faq(FAQ_METODO))
    h = head("Nosso Método | Instituto Correr, Fisioterapia em Blumenau",
             "Conheça o método do Instituto Correr: entender a dor, saúde individual, base científica e tecnologia humanizada. Avaliação detalhada antes de qualquer conduta.",
             SITE + "/metodo.html", sch)
    h += header("metodo.html")
    h += phero([("Nosso método", None)], "Como tratamos",
               "Ir além da fisioterapia convencional",
               "O que a gente quer é fazer diferença no seu mover. Isso começa por perseguir a causa, e não o sintoma, para que a melhora seja completa e sem recaída.")
    h += """
<main id="main">

<section class="section">
  <div class="container">
    <div class="sec-head sec-head--center">
      <span class="eyebrow eyebrow--center reveal">Os quatro pilares</span>
      <h2 class="reveal" data-d="1">Aquilo em que a gente não abre mão</h2>
    </div>
    <div class="grid grid-2 mt-8" style="gap:clamp(1.5rem,3vw,2.5rem)">
      <article class="card reveal"><span class="ic">@@ICBRAIN@@</span><h3>01. Entender a dor</h3><p>A dor é um sinal de proteção, não um inimigo a ser silenciado. Ela avisa que algo está sendo exigido além do que o tecido suporta naquele momento. Nosso trabalho é ler esse sinal com você e ensinar a administrar os próprios limites. É assim que o alerta se resolve na origem, em vez de voltar meses depois.</p></article>
      <article class="card reveal" data-d="1"><span class="ic">@@ICTARGET@@</span><h3>02. Saúde é individual</h3><p>Não existe só um jeito de ser saudável. Duas pessoas com a mesma queixa raramente têm a mesma causa, a mesma rotina ou a mesma resposta ao tratamento. Por isso não trabalhamos com protocolo rígido: cada paciente é tratado como um sistema único e complexo.</p></article>
      <article class="card reveal" data-d="2"><span class="ic">@@ICMICRO@@</span><h3>03. Base científica</h3><p>Embasamento científico é o ponto de partida de toda conduta: o que a literatura mostra que funciona, para quem e em que dose. E flexibilidade para adaptar avaliação e protocolo àquilo que o seu corpo de fato responde.</p></article>
      <article class="card reveal" data-d="3"><span class="ic">@@ICZAP@@</span><h3>04. Tecnologia humanizada</h3><p>Tecnologia avançada dá suporte aos protocolos e mede o que os olhos não veem. Mas o que determina o resultado continua sendo a avaliação inicial e a decisão clínica de quem está com você na sala.</p></article>
    </div>
  </div>
</section>

<section class="section section--sand">
  <div class="container container--narrow">
    <div class="sec-head sec-head--center">
      <span class="eyebrow eyebrow--center reveal">Em vídeo</span>
      <h2 class="reveal" data-d="1">Conheça o Instituto por dentro</h2>
      <p class="reveal" data-d="2">Uma volta pela estrutura e pelo clima do atendimento em Blumenau.</p>
    </div>
    <div class="mt-8">@@VIDEO@@</div>
  </div>
</section>

<section class="section section--soft">
  <div class="container">
    <div class="split split--top">
      <div class="sticky-col">
        <span class="eyebrow reveal">A jornada</span>
        <h2 class="reveal mt-5" data-d="1">Cinco etapas, sem caixa-preta</h2>
        <p class="lead reveal mt-5" data-d="2">Você acompanha o raciocínio em cada passo. Nada é feito sem que você entenda por que está sendo feito.</p>
        <div class="btn-row reveal mt-6" data-d="3"><a class="btn btn--wa" href="@@WA@@" target="_blank" rel="noopener">@@ICWA@@ Agendar minha avaliação</a></div>
      </div>
      <div class="steps reveal">
        <div class="step"><div class="step__n">1</div><div><h3>Anamnese</h3><p>Conversa aprofundada sobre a sua história: quando começou, o que piora, o que alivia, o que você já tentou, como é o seu dia, o que você precisa voltar a fazer. Metade do diagnóstico está aqui.</p></div></div>
        <div class="step"><div class="step__n">2</div><div><h3>Exame físico e funcional</h3><p>Testes de mobilidade, força, controle motor e provocação. Observamos como você se move de verdade, não só a articulação que dói, mas a cadeia inteira que a sustenta.</p></div></div>
        <div class="step"><div class="step__n">3</div><div><h3>Diagnóstico funcional e plano</h3><p>Fechamos a hipótese, explicamos para você em linguagem clara e definimos objetivos, técnicas, frequência e prazo. Você aprova o plano antes de começar.</p></div></div>
        <div class="step"><div class="step__n">4</div><div><h3>Tratamento com reavaliação</h3><p>Terapia manual, quiropraxia, exercício terapêutico, pilates ou a combinação que o seu caso pedir. Em intervalos definidos, medimos de novo e ajustamos o que for preciso.</p></div></div>
        <div class="step"><div class="step__n">5</div><div><h3>Alta com autonomia</h3><p>A alta não é o fim do assunto: você sai sabendo o que gerou o problema, o que evitar e o que manter. Se fizer sentido, segue no estúdio para consolidar o ganho.</p></div></div>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="split">
      <div>
        <span class="eyebrow reveal">O que a avaliação entrega</span>
        <h2 class="reveal mt-5" data-d="1">Você sai da primeira sessão sabendo o que tem</h2>
        <p class="lead reveal mt-5" data-d="2">Sem jargão desnecessário e sem resposta vaga. Clareza é parte do tratamento.</p>
        <ul class="checks reveal mt-6" data-d="3">
          <li>@@ICCHK@@ <span><strong>A hipótese diagnóstica funcional:</strong> o que está gerando a sua dor e por quê.</span></li>
          <li>@@ICCHK@@ <span><strong>O plano de tratamento:</strong> técnicas, frequência e duração estimada.</span></li>
          <li>@@ICCHK@@ <span><strong>Os marcos de evolução:</strong> o que esperar em 2, 4 e 8 semanas.</span></li>
          <li>@@ICCHK@@ <span><strong>O que fazer em casa:</strong> orientações práticas e ajustes de rotina.</span></li>
          <li>@@ICCHK@@ <span><strong>Encaminhamento, se necessário:</strong> quando o caso pede exame ou outro profissional, a gente diz.</span></li>
        </ul>
      </div>
      <div class="reveal" data-d="1">@@FAQ@@</div>
    </div>
  </div>
</section>

</main>
"""
    h += cta_band()
    h += footer()
    return _fill(h, faq=acc(FAQ_METODO))


# ==========================================================================
# EQUIPE
# ==========================================================================
def build_equipe():
    sch = S.tags(S.ORG, S.ROGER, S.CARLA, S.WEBSITE, S.breadcrumb([("Equipe", "equipe.html")]))
    h = head("Equipe | Instituto Correr, Fisioterapeutas em Blumenau",
             "Conheça a equipe do Instituto Correr: fisioterapeutas, quiropraxia e atendimento. Responsável técnico Roger Levi Andrade, CREFITO 175512. Blumenau/SC.",
             SITE + "/equipe.html", sch)
    h += header("equipe.html")
    h += phero([("Equipe", None)], "Quem cuida de você",
               "Especialistas com olhar humano",
               "Uma equipe multidisciplinar que discute os casos entre si, estuda continuamente e trata cada paciente como uma pessoa inteira, não como um segmento que dói.")
    h += """
<main id="main">
<section class="section">
  <div class="container">
    <div class="grid grid-4">@@TEAM@@</div>
  </div>
</section>

<section class="section section--soft">
  <div class="container">
    <div class="split">
      <div>
        <span class="eyebrow reveal">Compromisso</span>
        <h2 class="reveal mt-5" data-d="1">Formação continuada não é diferencial, é obrigação</h2>
        <p class="lead reveal mt-5" data-d="2">A fisioterapia muda rápido. O que era consenso há dez anos, hoje é revisto. Por isso a equipe estuda, discute casos e revisa conduta com frequência.</p>
        <ul class="checks reveal mt-6" data-d="3">
          <li>@@ICCHK@@ <span>Discussão interna de casos entre as especialidades</span></li>
          <li>@@ICCHK@@ <span>Atualização contínua em evidência científica</span></li>
          <li>@@ICCHK@@ <span>Registro profissional ativo e responsabilidade técnica</span></li>
          <li>@@ICCHK@@ <span>Encaminhamento quando o caso exige outra especialidade</span></li>
        </ul>
      </div>
      <div>
        <div class="infocard reveal"><span class="ic">@@ICAWARD@@</span><div><h3>Responsável técnico</h3><p>Roger Levi Andrade, CREFITO 175512. Fisioterapeuta com dez anos de prática clínica, especializado em acupuntura e técnicas manuais.</p></div></div>
        <div class="infocard reveal mt-5" data-d="1"><span class="ic">@@ICUSERS@@</span><div><h3>Atendimento</h3><p>Equipe de recepção e agendamento dedicada, para que o seu primeiro contato já seja resolvido, sem fila de espera para uma resposta simples.</p></div></div>
        <div class="infocard reveal mt-5" data-d="2"><span class="ic">@@ICCLK@@</span><div><h3>Horário</h3><p>@@HOURS@@</p></div></div>
      </div>
    </div>
  </div>
</section>
</main>
"""
    h += cta_band("Quer conversar com a nossa equipe?",
                  "Conte o que você está sentindo pelo WhatsApp. A gente indica qual profissional e qual abordagem fazem mais sentido para o seu caso.")
    h += footer()
    return _fill(h, team=cards_equipe(bio=True))


# ==========================================================================
# TRATAMENTOS (hub)
# ==========================================================================
def build_tratamentos():
    sch = S.tags(S.ORG, S.ROGER, S.CARLA, S.WEBSITE, S.breadcrumb([("Tratamentos", "tratamentos.html")]))
    h = head("Tratamentos | Fisioterapia, Quiropraxia e Pilates em Blumenau",
             "Fisioterapia, quiropraxia, pilates, liberação miofascial e terapias manuais em Blumenau/SC. Veja qual tratamento faz sentido para o seu caso no Instituto Correr.",
             SITE + "/tratamentos.html", sch)
    h += header("tratamentos.html")
    h += phero([("Tratamentos", None)], "O que fazemos",
               "Cinco especialidades, uma decisão clínica",
               "A técnica certa é consequência da avaliação. Aqui você entende o que cada abordagem resolve, e nós definimos juntos qual combinação é a sua.")
    h += """
<main id="main">
<section class="section">
  <div class="container">
    <div class="grid grid-3">@@TCARDS@@</div>
  </div>
</section>

<section class="section section--dark">
  <div class="container">
    <div class="sec-head sec-head--center">
      <span class="eyebrow eyebrow--center reveal">Como escolher</span>
      <h2 class="reveal" data-d="1">Não escolha sozinho</h2>
      <p class="reveal" data-d="2">A mesma dor no ombro pode pedir terapia manual, exercício ou ajuste de coluna. Depende inteiramente do que a avaliação encontrar. Comece por ela.</p>
    </div>
    <div class="grid grid-3 mt-8">
      <div class="pillar reveal"><div class="pillar__n">01</div><h3>Você descreve</h3><p>Conta o que sente, quando começou e o que já tentou.</p></div>
      <div class="pillar reveal" data-d="1"><div class="pillar__n">02</div><h3>A gente examina</h3><p>Exame físico e funcional para achar a causa, não o sintoma.</p></div>
      <div class="pillar reveal" data-d="2"><div class="pillar__n">03</div><h3>Definimos juntos</h3><p>Você aprova o plano, com técnicas, frequência e prazo, antes de começar.</p></div>
    </div>
    <div class="btn-row mt-8 reveal" style="justify-content:center"><a class="btn btn--wa btn--lg" href="@@WA@@" target="_blank" rel="noopener">@@ICWA@@ Agendar avaliação no WhatsApp</a></div>
  </div>
</section>
</main>
"""
    h += footer()
    return _fill(h, tcards=cards_tratamentos())


# ==========================================================================
# PÁGINAS DE TRATAMENTO (DESTINO PRINCIPAL DAS CAMPANHAS GOOGLE ADS)
# ==========================================================================
FAQ_CONVENIO = (
    "Vocês atendem convênios ou planos de saúde?",
    "Nosso atendimento é particular, planejado para dedicar o tempo necessário à sua avaliação e ao acompanhamento individual. Emitimos recibo para que você solicite reembolso junto ao seu plano de saúde. Chame no WhatsApp para consultar valores e horários."
)

TDATA = {
"fisioterapia": dict(
  title="Fisioterapia em Blumenau | Instituto Correr",
  desc="Fisioterapia em Blumenau/SC com avaliação detalhada e conduta individualizada. Tratamos a causa da dor para um retorno seguro e sem recidivas. Agende pelo WhatsApp.",
  h1="Fisioterapia individualizada para tratar a causa da sua dor",
  lead="Avaliação detalhada do seu movimento em Blumenau para aliviar a dor com segurança, corrigir a origem da sobrecarga e devolver sua rotina sem recaídas.",
  queixas=[
    ("Dor na coluna (lombar ou cervical)", "Dor ao ficar sentado, agachar, dormir ou carregar peso"),
    ("Dor no ombro, joelho ou quadril", "Estalos, perda de força ou dor ao caminhar e subir escadas"),
    ("Lesões esportivas e corrida", "Estiramentos, entorses, canelite, fascite e retorno ao esporte"),
    ("Reabilitação pós-operatória", "Joelho, ombro, coluna e quadril com protocolo seguro"),
    ("Tendinites, bursites e sobrecarga", "Dores repetitivas no trabalho ou no treino"),
    ("Outra dor ou dúvida sobre o meu caso", "Converse direto com a equipe para entender a indicação"),
  ],
  intro_h="Alívio é o começo, resolução é o objetivo",
  intro_p=[
    "Quase todo mundo já passou por uma sessão que aliviou na hora e não sustentou o resultado. Isso acontece quando o tratamento age sobre o local que dói sem investigar o que sobrecarregou aquele tecido.",
    "Nossos fisioterapeutas trabalham sobre as alterações biomecânicas que, se não corrigidas, viram quadro crônico ou lesão de repetição. A avaliação é personalizada e guiada por protocolos científicos atuais.",
    "O objetivo declarado do tratamento é um só: <strong>retorno breve e seguro às atividades cotidianas, com recuperação total e sem recidivas</strong>.",
  ],
  bene=[
    ("Dor tratada na origem", "Investigação da cadeia inteira de movimento, não só do ponto doloroso."),
    ("Conduta baseada em evidência", "Técnicas escolhidas pelo que a literatura mostra que funciona no seu tipo de caso."),
    ("Terapia humanizada e precisa", "Você entende cada etapa, participa das decisões e sabe o que esperar."),
    ("Recuperação funcional completa", "A alta acontece quando você volta ao que fazia antes, não quando a dor some."),
  ],
  para=[
    "Dor lombar, cervical, torácica e de ombro",
    "Lesões esportivas musculares, ligamentares e tendíneas",
    "Reabilitação pós-operatória (joelho, ombro, coluna, quadril)",
    "Tendinopatias e quadros de sobrecarga por repetição",
    "Dores crônicas que já não respondem a analgésico",
    "Perda de mobilidade, força ou equilíbrio",
    "Retorno ao esporte após lesão",
    "LER / DORT e queixas relacionadas ao trabalho",
  ],
  faq=[
    ("Preciso de encaminhamento médico para agendar?", "Não. O fisioterapeuta é profissional de primeiro contato e você pode agendar sua avaliação direto pelo WhatsApp. Se identificarmos necessidade de exame ou avaliação médica, orientamos e encaminhamos."),
    FAQ_CONVENIO,
    ("Quantas sessões de fisioterapia vou precisar?", "O número sai da avaliação, não de um pacote pré-definido. Quadros agudos simples costumam responder em poucas semanas; casos crônicos ou pós-operatórios pedem um plano mais longo, sempre com reavaliação periódica."),
    ("A fisioterapia serve para prevenir lesão?", "Serve, e é o uso mais subutilizado dela. Corrigir mecânica e ajustar carga antes que a dor apareça é mais rápido, mais barato e mais eficaz do que reabilitar depois."),
    ("Posso continuar treinando durante o tratamento?", "Na maioria dos casos, sim, com ajuste de carga e de gesto. Parar completamente raramente é a melhor conduta. O que muda é como e quanto você treina."),
  ]),

"quiropraxia": dict(
  title="Quiropraxia em Blumenau | Instituto Correr",
  desc="Quiropraxia em Blumenau/SC: ajustes precisos para dor de coluna, cervicalgia, cefaleias, hérnia de disco e ciática. Avaliação detalhada no Instituto Correr.",
  h1="Quiropraxia clínica para aliviar a dor e destravar a coluna",
  lead="Ajustes articulares precisos precedidos de avaliação física detalhada em Blumenau. Indicado para dor nas costas, cervical, ciática, hérnia de disco e tensão postural.",
  queixas=[
    ("Dor nas costas ou coluna travada", "Dificuldade para virar, levantar da cama ou ficar em pé"),
    ("Hérnia de disco ou dor ciática", "Dor que desce para o glúteo, coxa ou perna"),
    ("Dor no pescoço e torcicolo", "Rigidez cervical, dor nos ombros e limitação ao girar a cabeça"),
    ("Dor de cabeça de origem cervical", "Cefaleias frequentes ligadas à tensão na nuca"),
    ("Sobrecarga postural no trabalho", "Desconforto acumulado por horas sentado ou dirigindo"),
    ("Outra queixa articular ou dúvida", "Fale no WhatsApp para avaliarmos se a quiropraxia é indicada"),
  ],
  intro_h="Ajuste não é apenas estalo, é decisão clínica",
  intro_p=[
    "A quiropraxia atua sobre articulações que perderam mobilidade e passaram a sobrecarregar as vizinhas. Restaurar esse movimento devolve função à região e reduz o estímulo doloroso.",
    "Antes de qualquer ajuste, existe uma avaliação detalhada: conversa sobre a sua história, exame físico e exame funcional. É ela que determina o que ajustar, com que técnica e com que intensidade.",
    "No Instituto Correr, quando necessário, integramos o ajuste quiroprático com fisioterapia e fortalecimento para que o alívio se sustente no longo prazo.",
  ],
  bene=[
    ("Mobilidade articular restaurada", "A articulação volta a se mover no arco que deveria, e para de sobrecarregar as vizinhas."),
    ("Alívio sem medicação", "Abordagem conservadora e não invasiva, frequentemente com melhora perceptível já no início."),
    ("Postura mais equilibrada", "Reorganização da mecânica da coluna, com reflexo direto na forma como você se sustenta."),
    ("Integração com fisioterapia", "O ajuste abre a janela de alívio; o exercício consolida o ganho para evitar recaída."),
  ],
  para=[
    "Dores nas costas, no pescoço e na coluna",
    "Dores de cabeça frequentes de origem cervical",
    "Problemas posturais e rigidez articular",
    "Hérnia de disco e dor ciática (após avaliação clínica)",
    "Lesões por esforço repetitivo",
    "Gestantes com queixas de coluna",
    "Idosos com dores articulares e perda de mobilidade",
    "Atletas em busca de mobilidade e performance",
  ],
  faq=[
    ("O ajuste quiroprático dói?", "Não deve doer. O que a maioria sente é um alívio imediato de pressão. Pode haver um desconforto muscular leve nas horas seguintes, semelhante ao de um exercício novo, e ele passa rapidamente."),
    ("Quiropraxia serve para hérnia de disco e ciático?", "Pode fazer parte do tratamento, com técnica e dosagem adequadas ao seu estágio clínico. Isso é definido com segurança na avaliação inicial. Quando o caso pede fisioterapia associada, alinhamos tudo na hora."),
    FAQ_CONVENIO,
    ("Aquele estalo é osso saindo do lugar?", "Não. O som vem da liberação natural de gás dentro da cápsula articular quando a articulação recupera movimento. Nada sai do lugar: o objetivo é destravar o que estava rígido."),
    ("Gestante pode fazer quiropraxia?", "Sim, com técnicas suaves e posicionamento específico. É uma queixa muito comum devido à mudança de carga sobre a lombar e a pelve na gestação."),
  ]),

"pilates": dict(
  title="Pilates em Blumenau | Estúdio do Instituto Correr",
  desc="Estúdio de pilates em Blumenau/SC com aparelhos completos e séries individualizadas a partir da avaliação de movimento. Prevenção, tratamento e performance.",
  h1="Pilates clínico com séries feitas para o seu corpo",
  lead="Estúdio completo de aparelhos em Blumenau conduzido por fisioterapeutas. Avaliamos o seu movimento antes de montar cada aula para fortalecer sem dor.",
  queixas=[
    ("Fortalecer a coluna e o core", "Proteger lombar e cervical contra crises de dor"),
    ("Continuar após a fisioterapia", "Manter o ganho da reabilitação sem voltar à estaca zero"),
    ("Melhorar postura e flexibilidade", "Sair do sedentarismo com acompanhamento próximo"),
    ("Pilates para gestantes ou pós-parto", "Exercício seguro adaptado a cada fase"),
    ("Equilíbrio e autonomia para 60+", "Força, mobilidade e prevenção de quedas"),
    ("Condicionamento complementar ao esporte", "Estabilidade e controle motor para correr ou treinar melhor"),
  ],
  intro_h="A série é sua, não da turma",
  intro_p=[
    "Cada paciente é único. Por isso, no estúdio do Instituto Correr, o plano de trabalho é montado a partir da sua avaliação: o que você precisa ganhar, o que precisa proteger e o que precisa aprender a controlar.",
    "O método trabalha atenção à respiração e ativação conjunta de vários grupos musculares. Na prática, isso significa controle postural, alongamento e condicionamento físico e mental construídos ao mesmo tempo.",
    "Funciona como continuidade natural de uma reabilitação e também como porta de entrada segura para quem quer se exercitar sem risco de se machucar.",
  ],
  bene=[
    ("Controle postural real", "Não é 'sentar direito': é ganhar consciência e força para sustentar a postura sem esforço."),
    ("Core e estabilidade", "Ativação profunda que protege a coluna nas atividades do dia e no esporte."),
    ("Mobilidade e alongamento", "Amplitude ganha com controle, que é o que evita a lesão na hora do movimento rápido."),
    ("Continuidade após a alta", "O caminho mais eficiente para não voltar ao ponto de partida depois da reabilitação."),
  ],
  para=[
    "Quem terminou a reabilitação e quer manter o ganho",
    "Dores posturais e desconforto recorrente de coluna",
    "Sedentários que querem começar com segurança",
    "Gestantes e pós-parto (com avaliação prévia)",
    "Atletas buscando estabilidade e controle motor",
    "Idosos com foco em equilíbrio, força e autonomia",
    "Quem tem pouca mobilidade e muita tensão muscular",
    "Prevenção de lesões em quem treina corrida ou musculação",
  ],
  faq=[
    ("Qual a diferença do pilates aqui para o de uma academia?", "A avaliação funcional por trás. Suas séries são desenhadas e acompanhadas por fisioterapeutas a partir de um exame de movimento, não de uma aula genérica igual para todos."),
    ("Nunca fiz pilates. Consigo começar?", "Sim. A avaliação existe justamente para calibrar o ponto de partida. As séries iniciais respeitam o que você já consegue fazer hoje e evoluem conforme sua resposta."),
    FAQ_CONVENIO,
    ("Pilates substitui a fisioterapia?", "Em quadro de dor aguda instalada, a fisioterapia trata primeiro; o pilates entra como continuidade para consolidar e manter o ganho. Em muitos casos, ambos caminham juntos."),
    ("Quantas vezes por semana é indicado?", "Duas a três sessões semanais é a frequência mais comum para gerar adaptação consistente. Definimos a melhor rotina com você na avaliação."),
  ]),

"liberacao-miofascial": dict(
  title="Liberação Miofascial em Blumenau | Instituto Correr",
  desc="Liberação miofascial em Blumenau/SC: técnica que desativa pontos-gatilho e libera a fáscia muscular, reduzindo tensão e dor. Avaliação no Instituto Correr.",
  h1="Liberação miofascial para soltar tensões e recuperar o movimento",
  lead="Tratamento direcionado a pontos-gatilho, nódulos musculares e rigidez em Blumenau, combinando alívio preciso com investigação da causa da sobrecarga.",
  queixas=[
    ("Tensão crônica em pescoço e ombros", "Peso nos trapézios, estresse acumulado e rigidez"),
    ("Nódulos dolorosos e pontos-gatilho", "Pontos que doem ao toque ou irradiam dor"),
    ("Recuperação muscular de treinos", "Pernas pesadas, corrida intensa, crossfit ou ciclismo"),
    ("Lombar presa e sensação de encurtamento", "Rigidez ao acordar ou após horas sentado"),
    ("Cefaleia tensional", "Dor de cabeça associada à musculatura cervical contraída"),
    ("Quero avaliar minha tensão muscular", "Fale no WhatsApp para indicarmos a melhor sessão"),
  ],
  intro_h="Tensão crônica tem causa, e a gente procura ela",
  intro_p=[
    "A fáscia é o tecido que envolve e conecta os músculos. Quando ela perde deslizamento, o movimento fica restrito e surgem pontos de tensão que doem localmente e referem dor para outras regiões.",
    "A liberação miofascial atua diretamente na redução de tensões musculoesqueléticas, devolvendo alcance ao movimento e aliviando a sobrecarga do dia a dia ou do treino.",
    "No Instituto Correr, o protocolo vai além do alívio momentâneo e investiga a <strong>causa raiz da tensão</strong> para restabelecer a função muscular normal.",
  ],
  bene=[
    ("Desativação de pontos-gatilho", "Trabalho direto sobre os nódulos que geram dor local e dor referida."),
    ("Ganho imediato de amplitude", "O tecido volta a deslizar e o movimento recupera alcance já na sessão."),
    ("Menos tensão acumulada", "Alívio para quem carrega sobrecarga de trabalho ou treino nos ombros e lombar."),
    ("Preparo para o exercício", "Solta o que trava, para que o fortalecimento construa sobre uma base livre."),
  ],
  para=[
    "Tensão muscular crônica em pescoço, ombros e lombar",
    "Pontos-gatilho e nódulos dolorosos",
    "Dor referida e rigidez matinal",
    "Atletas e corredores com sobrecarga muscular",
    "Quem passa o dia sentado em frente ao computador",
    "Preparação e recuperação para treinos e provas",
    "Cefaleia tensional",
  ],
  faq=[
    ("É a mesma coisa que massagem relaxante?", "Não. A massagem relaxante busca bem-estar geral; a liberação miofascial é uma técnica clínica aplicada por fisioterapeuta sobre cadeias e pontos identificados na avaliação."),
    ("A liberação miofascial dói?", "Pode gerar um desconforto momentâneo sobre o ponto tenso, mas a intensidade é sempre ajustada com você. Não precisa ser insuportável para funcionar."),
    FAQ_CONVENIO,
    ("Quantas sessões são necessárias?", "Muitos pacientes sentem alívio já na primeira sessão. Quando a tensão vem de fraqueza ou alteração postural, combinamos a liberação com exercícios para a dor não voltar."),
  ]),

"terapias-manuais": dict(
  title="Terapias Manuais em Blumenau | Instituto Correr",
  desc="Terapias manuais em Blumenau/SC: mobilização articular, técnicas de tecidos moles, acupuntura e ventosaterapia aplicadas com raciocínio clínico. Instituto Correr.",
  h1="Terapias manuais aplicadas com avaliação e critério clínico",
  lead="Mobilização articular, técnicas de tecidos moles, acupuntura e ventosaterapia em Blumenau para modular a dor e destravar o movimento com segurança.",
  queixas=[
    ("Dor aguda que limita o movimento", "Crise lombar, cervical ou articular que impede exercícios"),
    ("Articulação presa ou sem amplitude", "Ombro, coluna, quadril ou tornozelo com bloqueio"),
    ("Acupuntura para modulação de dor", "Aplicada por fisioterapeuta com especialização"),
    ("Tensão muscular e ventosaterapia", "Recursos combinados conforme indicação clínica"),
    ("Dor cervical e cefaleia associada", "Alívio manual preciso na região craniocervical"),
    ("Quero saber qual técnica serve para mim", "Converse com a nossa equipe pelo WhatsApp"),
  ],
  intro_h="A mão treinada avalia enquanto trata",
  intro_p=[
    "Terapia manual não é um pacote único de técnicas: é um conjunto de recursos clínicos escolhidos conforme o exame físico, incluindo mobilização articular, manipulação, técnicas de tecidos moles, acupuntura e ventosaterapia.",
    "A vantagem do trabalho manual é a leitura em tempo real: o profissional sente a resposta do tecido e ajusta a intensidade durante a própria sessão.",
    "Aqui essas técnicas abrem a janela de alívio para que o movimento ativo consolide o resultado sem recaídas.",
  ],
  bene=[
    ("Mobilização e manipulação articular", "Recuperação de mobilidade em articulações restritas, na dose certa para o seu caso."),
    ("Técnicas de tecidos moles", "Trabalho sobre músculo, fáscia e tendão para reduzir tensão e melhorar deslizamento."),
    ("Acupuntura e ventosaterapia", "Recursos complementares para controle da dor, aplicados por especialista."),
    ("Ponte para a reabilitação ativa", "Reduz a dor inicial para permitir o fortalecimento que sustenta a melhora."),
  ],
  para=[
    "Restrição de mobilidade articular",
    "Dor cervical, torácica e lombar",
    "Quadros dolorosos agudos que limitam o movimento",
    "Tensão muscular persistente e encurtamentos",
    "Cefaleia de origem cervical",
    "Dor no ombro e limitação de alcance",
    "Modulação de dor em quadros crônicos",
  ],
  faq=[
    ("Vocês fazem acupuntura?", "Sim. Nosso responsável técnico, Roger Levi Andrade (CREFITO 175512), possui especialização em acupuntura e utiliza a técnica quando a avaliação clínica indica benefício."),
    ("Terapia manual sozinha resolve?", "Em quadros pontuais, pode bastar. Na maioria das dores recorrentes, ela reduz a dor e devolve mobilidade enquanto o exercício terapêutico impede que o problema volte."),
    FAQ_CONVENIO,
    ("Ventosaterapia deixa marca?", "Pode deixar marcas circulares temporárias que somem em poucos dias. Explicamos tudo antes e só aplicamos os recursos com os quais você se sentir confortável."),
  ]),
}


TIMG = {
"fisioterapia": ("trat-fisioterapia.webp", 900, 1349,
  "Fisioterapeuta orientando exercício com faixa elástica na perna de um paciente deitado na maca"),
"quiropraxia": ("trat-quiropraxia.webp", 900, 1350,
  "Quiropraxista aplicando um ajuste na coluna de uma paciente deitada de bruços"),
"pilates": ("trat-pilates.webp", 900, 1350,
  "Instrutora corrigindo a postura de uma aluna em aparelho de pilates no estúdio"),
"liberacao-miofascial": ("trat-liberacao-miofascial.webp", 900, 1350,
  "Terapeuta trabalhando a musculatura do pescoço e do ombro de uma paciente"),
"terapias-manuais": ("trat-terapias-manuais.webp", 900, 1125,
  "Fisioterapeuta mobilizando o braço de uma paciente deitada na maca"),
}


def build_treatment(slug):
    t = TMAP[slug]
    d = TDATA[slug]
    img_file, img_w, img_h, img_alt = TIMG[slug]
    wa_msg = "Olá! Gostaria de agendar uma avaliação de " + t["nome"] + " no Instituto Correr."
    sch = S.tags(S.ORG, S.ROGER, S.CARLA, S.WEBSITE, S.service(t, img_file, d["desc"]),
                 S.breadcrumb([("Tratamentos", "tratamentos.html"), (t["nome"], slug + ".html")]),
                 S.faq(d["faq"]))
    h = head(d["title"], d["desc"], SITE + "/" + slug + ".html", sch,
             preload="assets/img/" + img_file, page_img=img_file)
    h += header(slug, overlay=True, wa_msg=wa_msg)
    h += thero([("Tratamentos", "tratamentos.html"), (t["nome"], None)],
               t["nome"] + " em Blumenau", d["h1"], d["lead"],
               img_file, img_w, img_h, img_alt, wa_msg,
               cta_label="Agendar " + t["nome"].lower() + " no WhatsApp")

    qcards = symptom_cards(d["queixas"], t["nome"])
    intro = "".join('<p class="reveal mt-5" data-d="' + str(min(i + 1, 3)) + '">' + p + '</p>'
                    for i, p in enumerate(d["intro_p"]))
    bene = "".join('<article class="card reveal" data-d="' + str(i % 4) + '"><span class="ic">' +
                   IC[["target", "microscope", "heart", "trending"][i % 4]] + '</span><h3>' + b[0] +
                   '</h3><p>' + b[1] + '</p></article>' for i, b in enumerate(d["bene"]))
    para = "".join('<li>@@ICCHK@@ <span>' + x + '</span></li>' for x in d["para"])
    others = "".join(
        '<article class="card tcard reveal" data-d="' + str(i % 4) + '"><span class="ic">' + IC[o["icon"]] +
        '</span><h3>' + o["nome"] + '</h3><p>' + o["curto"] + '</p>'
        '<a class="tlink" href="' + o["slug"] + '.html">Conhecer ' + o["nome"].lower() + ' @@ICARR@@</a></article>'
        for i, o in enumerate([x for x in TREATMENTS if x["slug"] != slug]))

    h += """
<main id="main">

<!-- ===== 1. TRIAGEM RÁPIDA DIRETO PARA O WHATSAPP ===== -->
<section class="section section--tight section--soft" id="queixas">
  <div class="container">
    <div class="sec-head sec-head--center">
      <span class="eyebrow eyebrow--center reveal">Atendimento rápido pelo WhatsApp</span>
      <h2 class="reveal" data-d="1">Qual é a sua principal queixa hoje?</h2>
      <p class="reveal" data-d="2">Toque na opção abaixo para iniciar a conversa no WhatsApp já com o seu caso preenchido. Nossa equipe orienta você na hora.</p>
    </div>
    @@QCARDS@@
  </div>
</section>

<!-- ===== 2. COMO FUNCIONA + O QUE ENTREGA NA 1ª CONSULTA ===== -->
<section class="section">
  <div class="container">
    <div class="split split--top">
      <div>
        <span class="eyebrow reveal">Sobre o tratamento</span>
        <h2 class="reveal mt-5" data-d="1">@@IH@@</h2>
        @@INTRO@@
        <h3 class="reveal mt-8" data-d="2">Principais indicações atendidas</h3>
        <ul class="checks reveal mt-5" data-d="2">@@PARA@@</ul>
      </div>
      <div class="eval-card sticky-col reveal" data-d="1">
        <span class="eyebrow">Sua 1ª sessão aqui</span>
        <h3>O que acontece na avaliação inicial</h3>
        <p>Nada de pacote pronto antes de examinar você. Na primeira consulta entregamos clareza sobre o seu quadro:</p>
        <ol class="eval-steps">
          <li><span class="eval-steps__n">1</span><div><b>Escuta clínica</b><span>Entendemos sua rotina, histórico, exames prévios e o que agrava ou alivia a queixa.</span></div></li>
          <li><span class="eval-steps__n">2</span><div><b>Testes funcionais de movimento</b><span>Avaliamos mobilidade, força e a causa biomecânica real da sobrecarga.</span></div></li>
          <li><span class="eval-steps__n">3</span><div><b>Conduta e plano transparente</b><span>Explicamos o diagnóstico funcional, iniciamos o cuidado indicado e alinhamos os próximos passos.</span></div></li>
        </ol>
        <a class="btn btn--wa btn--lg" href="@@WAT@@" target="_blank" rel="noopener" style="width:100%">@@ICWA@@ Agendar minha avaliação</a>
        <div class="eval-card__meta">
          <span>@@ICCHK@@ Sem pedido médico</span>
          <span>@@ICCHK@@ Recibo p/ reembolso</span>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ===== 3. BENEFÍCIOS ===== -->
<section class="section section--soft">
  <div class="container">
    <div class="sec-head sec-head--center">
      <span class="eyebrow eyebrow--center reveal">Diferenciais clínicos</span>
      <h2 class="reveal" data-d="1">O que você ganha com @@TNOMEL@@ no Instituto Correr</h2>
    </div>
    <div class="grid grid-4 mt-8">@@BENE@@</div>
  </div>
</section>

<!-- ===== 4. PRÉ-AGENDAMENTO RÁPIDO + EQUIPE LOCAL ===== -->
@@FASTSRV@@

<!-- ===== 5. CONHEÇA A ESTRUTURA EM VÍDEO ===== -->
<section class="section">
  <div class="container container--narrow">
    <div class="sec-head sec-head--center">
      <span class="eyebrow eyebrow--center reveal">Estrutura em Blumenau</span>
      <h2 class="reveal" data-d="1">Veja onde você será atendido</h2>
      <p class="reveal" data-d="2">Consultórios equipados e estúdio completo na Rua Frederico Busch Júnior, 101.</p>
    </div>
    <div class="mt-8">@@VIDEO@@</div>
  </div>
</section>

<!-- ===== 6. FAQ DO TRATAMENTO ===== -->
<section class="section section--soft">
  <div class="container container--narrow">
    <div class="sec-head sec-head--center">
      <span class="eyebrow eyebrow--center reveal">Dúvidas frequentes</span>
      <h2 class="reveal" data-d="1">Perguntas comuns sobre @@TNOMEL@@</h2>
    </div>
    <div class="reveal mt-8">@@FAQ@@</div>
    <div class="center reveal mt-8">
      <a class="btn btn--wa" href="@@WAT@@" target="_blank" rel="noopener">@@ICWA@@ Tirar outra dúvida no WhatsApp</a>
    </div>
  </div>
</section>

<!-- ===== 7. OUTROS TRATAMENTOS ===== -->
<section class="section">
  <div class="container">
    <div class="sec-head sec-head--center">
      <span class="eyebrow eyebrow--center reveal">Cuidado integrado</span>
      <h2 class="reveal" data-d="1">Abordagens frequentemente combinadas</h2>
    </div>
    <div class="grid grid-4 mt-8">@@OTHERS@@</div>
  </div>
</section>

</main>
""".replace("@@QCARDS@@", qcards).replace("@@IH@@", d["intro_h"]).replace("@@INTRO@@", intro)\
   .replace("@@BENE@@", bene).replace("@@PARA@@", para).replace("@@OTHERS@@", others)\
   .replace("@@FASTSRV@@", fast_schedule_section(t["nome"], "section section--sand"))\
   .replace("@@TNOME@@", t["nome"]).replace("@@TNOMEL@@", t["nome"].lower())\
   .replace("@@WAT@@", wa_link(wa_msg))

    h += cta_band("Pronto para cuidar disso pelo caminho certo?",
                  "Chame nossa equipe no WhatsApp, conte o que está sentindo e veja os horários disponíveis ainda para esta semana em Blumenau.",
                  wa_msg=wa_msg)
    h += footer(wa_msg=wa_msg, wa_bar_label="Agendar " + t["nome"].lower())
    return _fill(h, faq=acc(d["faq"]))


# ==========================================================================
# CONTATO
# ==========================================================================
def build_contato():
    sch = S.tags(S.ORG, S.ROGER, S.CARLA, S.WEBSITE, S.breadcrumb([("Contato", "contato.html")]))
    h = head("Contato e Agendamento | Instituto Correr, Blumenau/SC",
             "Agende sua avaliação no Instituto Correr em Blumenau/SC. WhatsApp (47) 3222-3565, seg. a sex. das 7h às 12h e das 13h às 20h. Rua Frederico Busch Júnior, 101.",
             SITE + "/contato.html", sch)
    h += header("contato.html")
    h += phero([("Contato", None)], "Fale com a gente",
               "Agende sua avaliação",
               "Responda os campos abaixo e a gente já abre a conversa no WhatsApp com tudo preenchido, ou chame direto no botão, se preferir.")
    opts = "".join('<option value="' + t["nome"] + '">' + t["nome"] + '</option>' for t in TREATMENTS)
    h += """
<main id="main">
<section class="section">
  <div class="container">
    <div class="split split--form">
      <div>
        <span class="eyebrow reveal">Canais diretos</span>
        <h2 class="reveal mt-5" data-d="1">Onde nos encontrar</h2>
        <div class="grid mt-6" style="gap:1rem">
          <div class="infocard reveal" data-d="1"><span class="ic">@@ICWA@@</span><div><h3>WhatsApp (resposta rápida)</h3><a href="@@WA@@" target="_blank" rel="noopener">@@PH@@ · Abrir conversa agora</a></div></div>
          <div class="infocard reveal" data-d="2"><span class="ic">@@ICPH@@</span><div><h3>Telefone</h3><a href="tel:@@TEL@@">@@PH@@</a></div></div>
          <div class="infocard reveal" data-d="3"><span class="ic">@@ICMAIL@@</span><div><h3>E-mail</h3>@@EML@@</div></div>
          <div class="infocard reveal" data-d="3"><span class="ic">@@ICMAP@@</span><div><h3>Endereço</h3><p>@@STREET@@<br>@@CITY@@/@@STATE@@, CEP @@CEP@@</p></div></div>
          <div class="infocard reveal" data-d="3"><span class="ic">@@ICCLK@@</span><div><h3>Horário de atendimento</h3><p>@@HOURS@@<br>Sábados, domingos e feriados: fechado</p></div></div>
        </div>
      </div>
      <div class="form-panel reveal" data-d="1">
        <h2 style="font-size:clamp(1.5rem,2.4vw,1.9rem)">Solicitar agendamento</h2>
        <p class="mt-5" style="font-size:.97rem">Preencha e clique em enviar: a conversa abre no WhatsApp com a sua mensagem pronta.</p>
        <form class="form mt-6" data-wa-form="@@WANUM@@" data-form-name="contato_completo">
          <div class="field"><label for="nome">Nome completo <span class="req">*</span></label>
            <input id="nome" name="nome" type="text" required placeholder="Como podemos te chamar?" autocomplete="name"></div>
          <div class="field"><label for="telefone">Telefone / WhatsApp <span class="req">*</span></label>
            <input id="telefone" name="telefone" type="tel" required placeholder="(47) 90000-0000" data-mask="phone" autocomplete="tel"></div>
          <div class="field"><label for="servico">Tratamento de interesse</label>
            <select id="servico" name="servico">
              <option value="Ainda não sei, quero uma avaliação">Ainda não sei, quero uma avaliação</option>
              @@OPTS@@
            </select></div>
          <fieldset class="field shift-group">
            <legend>Melhor período para atendimento</legend>
            <div class="shift-pills">
              <label class="shift-pill"><input type="radio" name="periodo" value="Manhã (7h às 12h)" checked><span>Manhã (7h-12h)</span></label>
              <label class="shift-pill"><input type="radio" name="periodo" value="Tarde (13h às 17h)"><span>Tarde (13h-17h)</span></label>
              <label class="shift-pill"><input type="radio" name="periodo" value="Fim do dia (17h às 20h)"><span>Noite (17h-20h)</span></label>
            </div>
          </fieldset>
          <div class="field"><label for="mensagem">O que você está sentindo?</label>
            <textarea id="mensagem" name="mensagem" placeholder="Ex.: dor lombar há 3 meses, piora quando fico sentado..."></textarea></div>
          <button class="btn btn--wa btn--lg" type="submit">@@ICWA@@ Enviar pelo WhatsApp</button>
          <p class="form__note">Ao enviar, você será direcionado ao WhatsApp do Instituto Correr com a mensagem preenchida. Seus dados não são armazenados neste site.</p>
        </form>
      </div>
    </div>
  </div>
</section>

<section class="section section--tight section--soft">
  <div class="container">
    <div class="map-wrap reveal">
      <iframe title="Mapa do Instituto Correr, Blumenau/SC" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen
        src="https://www.google.com/maps?q=Rua%20Frederico%20Busch%20Junior%2C%20101%20-%20Blumenau%2C%20SC&output=embed"></iframe>
    </div>
  </div>
</section>
</main>
""".replace("@@OPTS@@", opts).replace("@@WANUM@@", WA)
    h += footer()
    return _fill(h)


# ==========================================================================
# 404
# ==========================================================================
def build_404():
    h = head("Página não encontrada | Instituto Correr", "A página que você procura não existe ou foi movida.",
             SITE + "/404.html")
    h = h.replace('<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">',
                  '<meta name="robots" content="noindex, follow">')
    h += header()
    h += """
<main id="main">
<section class="section" style="padding-top:calc(var(--nav-h) + 5rem);text-align:center">
  <div class="container container--narrow">
    <span class="eyebrow eyebrow--center">Erro 404</span>
    <h1 class="mt-5">Essa página saiu do lugar</h1>
    <p class="lead mt-5">O endereço que você acessou não existe ou foi movido. Mas a gente pode te levar de volta ao caminho certo.</p>
    <div class="btn-row mt-8" style="justify-content:center">
      <a class="btn btn--wa" href="@@WA@@" target="_blank" rel="noopener">@@ICWA@@ Falar no WhatsApp</a>
      <a class="btn btn--ghost" href="index.html">Voltar ao início</a>
    </div>
  </div>
</section>
</main>
"""
    h += footer()
    return _fill(h)


# ==========================================================================
# ARQUIVOS AUXILIARES
# ==========================================================================
def build_aux():
    pages = ["", "sobre.html", "metodo.html", "equipe.html", "tratamentos.html", "contato.html"] + \
            [t["slug"] + ".html" for t in TREATMENTS]
    prio = {"": "1.0", "tratamentos.html": "0.9", "contato.html": "0.9",
            "fisioterapia.html": "0.9", "quiropraxia.html": "0.9", "pilates.html": "0.9"}
    today = S.BUILD_DATE
    urls = ""
    for p in pages:
        urls += ('  <url><loc>' + SITE + '/' + p + '</loc>'
                 '<lastmod>' + today + '</lastmod>'
                 '<changefreq>monthly</changefreq>'
                 '<priority>' + prio.get(p, "0.8") + '</priority></url>\n')
    sm = ('<?xml version="1.0" encoding="UTF-8"?>\n'
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + urls + '</urlset>\n')
    write("sitemap.xml", sm)
    blocked = ["/build/", "/tools/", "/AGENTS.md", "/COMECE-AQUI.md", "/LEIA-ME.md", "/package.json"]
    robots = ["# Instituto Correr: fisioterapia, quiropraxia e pilates em Blumenau/SC",
              "# Resumo para assistentes de IA: " + SITE + "/llms.txt", ""]
    ai_bots = ["Googlebot", "Bingbot", "OAI-SearchBot", "ChatGPT-User", "GPTBot",
               "PerplexityBot", "Perplexity-User", "ClaudeBot", "Claude-SearchBot", "Claude-User",
               "Google-Extended", "Applebot", "Applebot-Extended", "meta-externalagent", "DuckAssistBot"]
    for bot in ai_bots + ["*"]:
        robots.append("User-agent: " + bot)
        robots.append("Allow: /")
        for b in blocked:
            robots.append("Disallow: " + b)
        robots.append("")
    robots += ["Sitemap: " + SITE + "/sitemap.xml", ""]
    write("robots.txt", "\n".join(robots))
    write("llms.txt", build_llms())

    fav = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">'
           '<rect width="100" height="100" rx="26" fill="#232F1B"/>'
           '<circle cx="60" cy="26" r="11" fill="#B6C7A3"/>'
           '<path d="M28 74c0-16 12-27 27-27" stroke="#86A06C" stroke-width="11" fill="none" stroke-linecap="round"/>'
           '<path d="M72 74c0-16-12-27-27-27" stroke="#FFFFFF" stroke-width="11" fill="none" stroke-linecap="round"/>'
           '</svg>')
    with open(os.path.join(OUT, "assets/img/favicon.svg"), "w", encoding="utf-8") as f:
        f.write(fav)
    print("  ✓ assets/img/favicon.svg")


def _txt(html):
    import re
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", html)).strip()


def build_llms():
    L = ["# " + NAME, "",
         "> Clínica de fisioterapia, quiropraxia, pilates, liberação miofascial e terapias manuais "
         "em " + CITY + "/" + STATE + ". Atendimento particular, com avaliação detalhada "
         "antes de qualquer conduta e plano de tratamento individualizado para prevenção, "
         "reabilitação e performance.", "",
         "## Dados da clínica", "",
         "- Nome: " + NAME,
         "- Endereço: " + ADDRESS_FULL,
         "- Telefone e WhatsApp: " + PHONE_DISPLAY + " (https://wa.me/" + WA + ")",
         "- E-mail: " + EMAIL,
         "- Horário: " + HOURS + ". Sábados, domingos e feriados: fechado.",
         "- Agendamento: direto pelo WhatsApp, sem necessidade de pedido médico.",
         "- Pagamento: atendimento particular, com recibo para reembolso do plano de saúde.",
         "- Atende pacientes de Blumenau, Gaspar, Indaial, Timbó e Pomerode.",
         "- Responsável técnico: Roger Levi Andrade, fisioterapeuta, CREFITO 175512.",
         "- Instagram: " + INSTAGRAM,
         "- Site: " + SITE + "/", "",
         "## Tratamentos", ""]
    for t in TREATMENTS:
        L.append("- [" + t["nome"] + " em Blumenau](" + SITE + "/" + t["slug"] + ".html): "
                 + t["curto"] + " Foco: " + "; ".join(t["bullets"]).lower() + ".")
    L += ["", "## Equipe", ""]
    for m in TEAM:
        L.append("- " + m["nome"] + ", " + m["role"].replace(" · ", ", ")
                 + (" (" + m["reg"] + ")" if m["reg"] else "") + ": " + m["bio"])
    L += ["", "## Como funciona o atendimento", "",
          "1. Avaliação detalhada: história, exame físico e funcional, testes de movimento.",
          "2. Diagnóstico funcional explicado ao paciente, com a causa provável da queixa.",
          "3. Plano de tratamento com técnicas, frequência e prazo definidos antes de começar.",
          "4. Reavaliações periódicas. Não há pacote fechado vendido antes da avaliação.",
          "5. Alta quando o paciente volta às atividades, com orientação para prevenir recidiva.", "",
          "## Perguntas frequentes", ""]
    seen = set()
    for q, a in FAQ_HOME + [x for t in TREATMENTS for x in TDATA[t["slug"]]["faq"]]:
        if q in seen:
            continue
        seen.add(q)
        L += ["### " + _txt(q), "", _txt(a), ""]
    L += ["## Páginas", "",
          "- [Início](" + SITE + "/)",
          "- [Sobre o Instituto](" + SITE + "/sobre.html)",
          "- [Nosso método](" + SITE + "/metodo.html)",
          "- [Equipe](" + SITE + "/equipe.html)",
          "- [Todos os tratamentos](" + SITE + "/tratamentos.html)",
          "- [Contato e agendamento](" + SITE + "/contato.html)", "",
          "Conteúdo informativo. Não substitui avaliação individual por um profissional de saúde.", ""]
    return "\n".join(L)


if __name__ == "__main__":
    print("Gerando site do Instituto Correr...\n")
    write("index.html", build_home())
    write("sobre.html", build_sobre())
    write("metodo.html", build_metodo())
    write("equipe.html", build_equipe())
    write("tratamentos.html", build_tratamentos())
    for t in TREATMENTS:
        write(t["slug"] + ".html", build_treatment(t["slug"]))
    write("contato.html", build_contato())
    write("404.html", build_404())
    build_aux()
    print("\nConcluído.")
