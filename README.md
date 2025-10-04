# 🌍 A.B.G.M.S.: Autonomous Biodiversity Global Monitoring System 🦜🌱

## Inspiration ✨
Biodiversity is collapsing, and conservationists struggle to track endangered species like the **Snowy Plover**.  
Manual field surveys are slow, costly, and often disturb wildlife.  

We imagined an autonomous AI system that monitors species in real time, logs sightings to an open dataset, and notifies conservation groups instantly — a global “radar” for protecting our planet’s wildlife.

---

## What It Does 🎯

- 🚁 **Drone/Video Feed Simulation:** Streams aerial/wildlife footage as if from a live drone.  
- 👁️ **Computer Vision:** Detects species (birds, mammals, etc.) in real time using **YOLOv8**.  
- 🧠 **AI Agents:** Summarize findings, generate natural-language logs, and orchestrate notifications.  
- 🗺️ **Live Dashboard:** Built with **Next.js + Leaflet** to show map pins where species are spotted, alongside live detection logs.  
- 🔔 **Alerts:** Endangered species sightings trigger automated SMS/email alerts to conservation groups.  
- 🌐 **Open Source Reports:** Community members can submit photos of sightings; AI verifies before adding them to the biodiversity dataset.

---

## How We Built It 🛠️

- 🎨 **Frontend:** Next.js, Tailwind CSS, Shadcn/ui, Leaflet, Butterfly — for a clean, responsive biodiversity dashboard.  
- 🎥 **Live Video Streaming:** Dockerized NGINX RTMP server + FFmpeg simulate drone/wildlife footage as a live feed.  
- 🚀 **CV Pipeline:** FastAPI server ingests frames, runs YOLOv8 object detection, invokes Groq LLaMA for summarization, and logs detections to Supabase.  
- 🗄️ **Database:** Supabase for real-time storage of sightings and automatic frontend updates.  
- 👁️ **Object Detection:** Ultralytics YOLOv8 trained/fine-tuned on species datasets (birds, mammals, etc.) for live inference.  
- 📞 **Conservation Alerts:** Dain agents + Twilio API send instant SMS/email notifications when endangered species are detected.  
- 🤝 **Crowdsourcing:** User-submitted photos are AI-verified before being logged as trusted sightings.

---

## Challenges We Ran Into 🧩

- Streaming wildlife video through FFmpeg + NGINX without lag.  
- Getting real-time pins on the Leaflet map synced with Supabase.  
- Balancing accuracy vs. speed in YOLOv8 detections.  
- Designing a system that feels both autonomous and community-driven.

---

## Accomplishments That We’re Proud Of 🏆

- Built a working end-to-end system: **video → AI detection → database → live map → conservation alerts**.  
- Created a clean, intuitive dashboard that displays detections in real time.  
- Integrated AI agents to make the system feel intelligent, not just technical.  
- Extended the platform with crowdsourced, AI-verified reports — making it open source and global.

---

## What We Learned 📚

- Real-time AI pipelines are powerful but tricky — everything must sync seamlessly.  
- Community-driven AI adds scalability and impact.  
- Always build a simple MVP first (detection + map pins) before layering on more features.

---

## What’s Next 🚀

- 🌐 **Global Expansion:** Scale from Bay Area wetlands to global biodiversity monitoring.  
- 🤖 **Autonomous Drones:** Integrate with real UAVs for fully automated data collection.  
- 📊 **Advanced Analytics:** Species population trends, heatmaps, and predictive modeling.  
- 💬 **Chatbot Assistant:** RAG-powered conservation chatbot to query the dataset in natural language.

---

## Built With ⚙️

**Frontend:** Next.js, Tailwind CSS, Shadcn/ui, Leaflet, Butterfly  
**Backend:** FastAPI, Supabase, Docker, NGINX, FFmpeg  
**AI:** Ultralytics YOLOv8, Groq LLaMA, Dain agents  
**Automation:** Twilio API  
**Collaboration:** Open-source community contributions  

---

⚡ **With EcoDrone, we’re building the world’s first AI-powered, open-source biodiversity monitoring platform — turning every drone, webcam, and smartphone into a global conservation monitoring system.**
