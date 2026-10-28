# MIR-Experiments-with-Music21

<p align="center">
  <img src="https://img.shields.io/badge/License-GPLv3-blue.svg?style=for-the-badge" alt="License: GPL v3">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Musicology-Digital_Humanities-orange?style=for-the-badge" alt="Digital Musicology">
  <img src="https://img.shields.io/badge/Framework-Music21-purple?style=for-the-badge" alt="Music21">
</p>

**MIR-Experiments-with-Music21** es un entorno interactivo y reproducible de Music Information Retrieval (MIR) orientado a la pedagogía y al análisis asistido por ordenador de la polifonía renacentista.

Este proyecto articula un flujo de trabajo (*workflow*) guiado e interactivo desplegado a través del cuaderno JupyterLab **`nb_full.ipynb`**, cuyo motor de cómputo analítico se basa en tres módulos de Python programados *ad hoc* por su autor (**`melodia_general.py`**, **`ngramas.py`** y **`acordes.py`**), integrados junto a librerías estándar del ecosistema científico (`music21`, `pandas`, `matplotlib`, `scikit-learn`) para el examen melódico, modal, armónico y de relación música-texto en repertorios históricos polifónicos.

---

## 🏛️ Origen del proyecto

Este software y su flujo metodológico tienen su origen en la comunicación presentada en:

> **Trabajo:** *Music21 en el aula: una aplicación a la Música del Renacimiento*  
> **Congreso:** I Congrés Internacional de la Societat Catalana de Musicologia  
> **Organización:** Societat Catalana de Musicologia (Institut d'Estudis Catalans)  
> **Ubicación:** Barcelona, Cataluña, España (26-29 de abril de 2022 / marco congresual 2021)  
> **Acceso a publicación/actas:** [Revista Catalana de Musicologia](https://revistes.iec.cat/index.php/RCMus/index)

Este prototipo constituyó el punto de partida técnico y metodológico crucial para la posterior investigación predoctoral de su autor, culminando en la tesis doctoral:

> **López-Rocamora, Pablo (2026).** *Tecnología digital aplicada al estudio, análisis y enseñanza de la polifonía española (siglos XVI-XVIII)*. Tesis Doctoral, Universidad de Murcia. Dirigida por Antonio Pardo Cayuela y Emilio Ros-Fábregas.

---

## 🚀 Capacidades y Módulos Desarrollados para el Workflow

El flujo articulado en `nb_full.ipynb` permite cargar partituras polifónicas mediante selectores dinámicos basados en `ipywidgets`, procesarlas con las rutinas de los módulos de autoría propia y exportar una matriz comparativa final en formato Excel (`output.xlsx`).

1. **Módulo de análisis melódico general y modal (`melodia_general.py`):**
   - **Nota *finalis*:** Detección de la nota conclusiva polifónica mediante reducción armónica vertical (`chordify`).
   - **Ámbito melódico total y por voces:** Cálculo del espectro interválico (*ambitus*) clasificando la disposición de las voces en *a voce piena* o *ad aequales*, además del desglose por tesituras individuales (Superius, Altus, Tenor, Bassus).
   - **Nota central de cada voz:** Obtención de la mediana de alturas (*pitches*) por línea vocal.
   - **Atribución de modo polifónico:** Extracción del modo polifónico basada en el *octoechos* (Protus, Deuterus, Tritus, Tetrardus; auténticos y plagales) partiendo de los razonamientos que Bernhard Meier expuso en su obra *The Modes of Classical Vocal Polyphony* (1988).
   - **Recurrencia melódica:** Histogramas comparativos de frecuencias de notas ordenados desde la *finalis*.
   - **Intervalos melódicos:** Frecuencia de saltos interválicos por voz con cómputo de silencios y movimientos ascendentes/descendentes.
   - **Relación música / texto (`MT_relation`):** Alineación texto-música mediante parsing de lírica (`search.lyrics.LyricSearcher`) y cómputo del perfil del contorno melódico asociado a cada lema textual (escalado normalizado en rango $[-1, 1]$ con `MinMaxScaler`).

2. **Módulo de secuencias melódicas y $N$-gramas (`ngramas.py`):**
   - **Extracción de $N$-gramas:** Segmentación en secuencias lineales de longitud $N$ parametrizable interactivamente mediante un control deslizante (*slider*).
   - **Ranking de secuencias:** Identificación de los patrones melódicos más y menos frecuentes por voz.
   - **Código parsons (Parsons Code):** Algoritmo de abstracción direccional del contorno melódico (`U`, `u`, `D`, `d`, `R`, `=`).

3. **Módulo de análisis armónico vertical (`acordes.py`):**
   - Reducción contrapuntística a bloques verticales (`chordify`).
   - Catalogación sistemática de tipologías armónicas renacentistas: tríadas mayores y menores (completas e incompletas), tríadas aumentadas/disminuidas y acordes con séptima.
   - Histogramas horizontales comparativos de recurrencia vertical entre obras.

4. **Persistencia y exportación (`base.py`):**
   - Estructuras auxiliares (`OrderedCounter`, `flat_values`, `dic2txt`) y consolidación de todos los metadatos y descriptores comparados en un `DataFrame` de Pandas para su guardado automático en hoja de cálculo `output.xlsx`.

---

## 📁 Archivos de Prueba Incluidos

El repositorio incluye dos ejemplos polifónicos en formato MusicXML listos para comparar en el cuaderno:
* **`josquin_kyrie.musicxml`**: *Kyrie* de la *Missa L'homme armé super voces musicales* de Josquin des Prés.
* **`morales_kyrie.musicxml`**: *Kyrie* de la *Missa L'homme armé* (a 4 voces) de Cristóbal de Morales.

---

## 🛠️ Stack Tecnológico
- **Lenguaje:** Python 3.10+
- **Módulos propios del proyecto:** `melodia_general.py`, `ngramas.py`, `acordes.py`, `base.py`
- **Musicología computacional:** `music21`
- **Análisis de datos y estadísticas:** `pandas`, `numpy`, `scikit-learn`
- **Interfaz y visualización:** `JupyterLab`, `ipywidgets`, `matplotlib`

---

## 📦 Instalación

Sigue estos pasos en tu terminal (Linux / macOS / Windows):

### 1. Clonar el repositorio y crear el entorno virtual

```bash
git clone https://github.com/lopezrpablo/MIR-Experiments-with-Music21.git
cd MIR-Experiments-with-Music21

python3 -m venv MIR-Experiments-with-Music21
source bin/activate  # En Windows: venv\Scripts\activate
```

### 2. Instalar dependencias

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 3. Registrar el kernel en Jupyter

```bash
python -m ipykernel install --user --name mir_music21 --display-name "Python (MIR-Music21)"
```

---

## 💻 Modo de Uso

El flujo principal está completamente integrado y documentado en el cuaderno interactivo:

1. Inicia el servidor de JupyterLab:
   ```bash
   jupyter lab
   ```
2. Abre el archivo **`nb_full.ipynb`**.
3. Asegúrate de tener seleccionado el kernel `Python (MIR-Music21)`.
4. Ejecuta las celdas secuencialmente. 

> **Controles interactivos en el cuaderno:**  
> - **Selectores de partitura:** Dos menús desplegables (`Dropdown`) para escoger las obras a contrastar (por defecto, `morales_kyrie.musicxml` y `josquin_kyrie.musicxml`).  
> - **Control de $N$-gramas:** Un control deslizante (`IntSlider`) sincronizado con un campo numérico (`IntText`) para fijar la ventana de notas de las secuencias melódicas antes de su extracción mediante `ngramas.py`.

---

## 📂 Estructura del Repositorio

```text
MIR-Experiments-with-Music21/
├── nb_full.ipynb              # Cuaderno principal con el workflow guiado
├── melodia_general.py         # Módulo de autor: Análisis modal, ambitus, interválica y texto/música
├── ngramas.py                 # Módulo de autor: Extracción de n-gramas melódicos y código Parsons
├── acordes.py                 # Módulo de autor: Extracción y clasificación de estructuras armónicas
├── base.py                    # Módulo de autor: Estructuras auxiliares (OrderedCounter, dic2txt)
├── josquin_kyrie.musicxml     # Partitura de prueba (Josquin)
├── morales_kyrie.musicxml     # Partitura de prueba (Morales)
├── requirements.txt           # Dependencias del entorno
├── LICENSE                    # Licencia GNU GPLv3
└── README.md
```

---

## 🤝 Contribuyendo y Citación

Para proponer mejoras, corregir incidencias o ampliar el soporte de formatos:
1. Haz un **Fork** de este repositorio.
2. Crea una rama para tus modificaciones (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza tus commits con mensajes descriptivos.
4. Abre un **Pull Request**.

### 📚 Cómo citar este trabajo
Si utilizas este software, sus módulos analíticos o su metodología en tus investigaciones, actividades docentes o publicaciones científicas, por favor cita el software registrado en Zenodo y la tesis doctoral de referencia:

```bibtex
@software{lopez_rocamora_mir_music21,
  author       = {López-Rocamora, Pablo},
  title        = {{MIR-Experiments-with-Music21: Workflow para el análisis computacional de la polifonía del Renacimiento}},
  month        = {oct},
  year         = {2026},
  publisher    = {Zenodo},
  version      = {v1.0.0},
  doi          = {10.5281/zenodo.XXXXXXX},
  url          = {[https://doi.org/10.5281/zenodo.XXXXXXX](https://doi.org/10.5281/zenodo.XXXXXXX)}
}

@phdthesis{lopez_rocamora_tesis_2026,
  author       = {López-Rocamora, Pablo},
  title        = {{Tecnología digital aplicada al estudio, análisis y enseñanza de la polifonía española (siglos XVI-XVIII)}},
  school       = {Universidad de Murcia},
  year         = {2026},
  type         = {Tesis Doctoral},
  note         = {Dirigida por Antonio Pardo Cayuela y Emilio Ros-Fábregas}
}

@inproceedings{lopez_rocamora_music21_aula_2022,
  author       = {López-Rocamora, Pablo},
  title        = {{Music21 en el aula: una aplicación a la Música del Renacimiento}},
  booktitle    = {{Actes del I Congrés Internacional de la Societat Catalana de Musicologia}},
  year         = {2022},
  address      = {Barcelona},
  publisher    = {Societat Catalana de Musicologia / Institut d'Estudis Catalans},
  url          = {[https://revistes.iec.cat/index.php/RCMus/index](https://revistes.iec.cat/index.php/RCMus/index)}
}
```

> **Nota para investigadores:** Recuerda sustituir `10.5281/zenodo.XXXXXXX` por el identificador DOI generado al publicar el release en Zenodo.

---

## 📝 Licencia
Este proyecto está distribuido bajo los términos de la licencia libre **GNU General Public License v3.0 (GPLv3)**. Consulta el archivo `LICENSE` para conocer los detalles legales completos.

---

## 📬 Contacto
**Pablo López-Rocamora, PhD**  
Universidad de Murcia  
Para consultas académicas o reportes de errores, puedes abrir una incidencia (*issue*) en este repositorio.
