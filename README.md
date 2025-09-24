# Launch Model

> **The Launch is the machine manifesto**

## 🌌 Constellation Information

- **Module Key**: `launch_model`  
- **Repository**: `launch-model`
- **Orbit**: `core`
- **Status**: `developing` 🚧
- **Emoji**: 🚀

## 🚀 Launch Model Development Status

**The Launch Model is now actively developing!** 🚧✨

This core system star has progressed from seed to developing status with the implementation of live constellation workflow analytics. The Launch Model serves as the operational intelligence center for FourTwenty Analytics, providing funnel-based tracking and performance monitoring for all constellation workflows.

### 📊 Live Funnel Specifications

The Launch Model now contains **real operational data** instead of seeded examples:

#### Active Constellation Workflow Funnels

- **🔄 Signal Aggregation** - Signal Model's nightly constellation signal collection workflow
- **📜 Script Aggregation** - Archive Model's manual script collection and deduplication process  
- **🧹 Script Scrubbing** - Archive Model's interactive optimization and cleanup workflow
- **🫀 Constellation Status Pulse** - Archive Model's automated status monitoring and synchronization
- **📡 Broadcast Creation** - Hub's interactive signal broadcast creation workflow
- **🌟 Module Creation** - Hub's new constellation star scaffolding and integration workflow

Each funnel includes:

- **Detailed Phase Definitions** - Real workflow steps with technical requirements
- **SLA Monitoring** - Time limits based on actual performance data
- **Failure Remediation** - Specific recovery procedures for each workflow
- **Performance Metrics** - Workflow duration, phase transitions, error recovery tracking

### 🎯 Operational Intelligence Features

- **Workflow Analytics** - Track performance, bottlenecks, and optimization opportunities
- **SLA Breach Detection** - Monitor when workflows exceed expected timeframes
- **Failure Pattern Analysis** - Identify common failure points and recovery effectiveness
- **Real-time Monitoring** - Live operational data from actual constellation workflows

**📋 Complete Specifications**: `seeds/funnel_spec.yml` & `schema/funnel_spec.schema.yml`

## 🧠 Workflow Intelligence System

**The Launch Model provides operational intelligence through automated workflow funnel analysis.**

### 📊 Constellation Workflow Analysis

The Launch Model continuously monitors and analyzes constellation workflow performance using intelligent signal processing:

#### 🔍 Core Analysis Engine

**Script**: `scripts/workflow-funnel-analyzer.sh`

- **Auto-Discovery**: Automatically finds the latest signal aggregation from Signal Model
- **Smart Matching**: Maps workflow signals to funnel types using title and metadata patterns
- **Performance Tracking**: Generates timestamped analysis reports with comprehensive metrics
- **Data Storage**: Outputs structured CSV data and diagnostic reports to `data/internal/`

#### 🎯 Funnel Matching Logic

The system intelligently categorizes constellation signals into workflow funnels:

- **`signal_aggregation`** ↔ "Constellation Signal Aggregation"
- **`script_aggregation`** ↔ "Script Collection Optimization Complete" (aggregation type)
- **`script_scrubbing`** ↔ "Script Collection Optimization Complete" (scrubbing type)
- **`constellation_status_pulse`** ↔ "Constellation Status Pulse Complete"
- **`module_creation`** ↔ title="New constellation star initialized"
- **`broadcast_creation`** ↔ module_key + title ≠ "New constellation star initialized"

#### 📈 Analysis Outputs

**CSV Data Table**: `data/internal/workflow-analysis-YYYYMMDDTHHMMSSZ.csv`

```csv
timestamp,funnel_id,signal_id,module,repo,title,rating,broadcast_key,status,notes
```

**Diagnostic Reports**: `data/internal/diagnostics-YYYYMMDDTHHMMSSZ.txt`

- Funnel distribution analysis
- Rating severity breakdown
- Module activity tracking
- Recent workflow event timeline

#### 🚀 Quick Analysis Commands

```bash
# Run complete workflow analysis
./scripts/workflow-funnel-analyzer.sh

# View latest results (simplified)
./scripts/quick-analysis.sh

# Setup nightly automation
./scripts/setup-workflow-cron.sh
```

### 🌙 Nightly Automation

**Automated Workflow Intelligence** runs daily at 2:00 AM UTC:

#### 📅 Nightly Analysis Pipeline

**Script**: `scripts/nightly-workflow-analysis.sh`

1. **Signal Collection**: Finds latest constellation aggregation from Signal Model
2. **Funnel Processing**: Analyzes all workflow signals using intelligent matching
3. **Report Generation**: Creates timestamped CSV data and diagnostic summaries  
4. **Data Management**: Maintains 30-day rolling analysis history
5. **Status Logging**: Records all operations in `logs/nightly-workflow-analysis.log`

#### ⚙️ Cron Configuration

**Setup Script**: `scripts/setup-workflow-cron.sh`

- Interactive cron job installation
- Conflict detection and resolution
- Silent mode execution for automation
- Comprehensive logging and error handling

### 📊 Current Performance Insights

**Latest Analysis Results** (as of system deployment):

- **Total Signals Processed**: 20 signals from 20 constellation stars
- **Funnel Distribution**:
  - 18 `module_creation` events (constellation expansion)
  - 2 `broadcast_creation` events (operational signals)
- **Module Coverage**: Perfect 100% - all 20 stars contributing signals
- **Critical Events**: Archive Model "Nightly Heartbeats", Signal Model "Broadcasting System"

### 🎯 Advanced Intelligence Capabilities

- **Real-time Monitoring**: Live analysis of constellation workflow performance
- **Performance Metrics**: Track workflow duration, success rates, and bottlenecks  
- **Pattern Recognition**: Identify operational trends and optimization opportunities
- **Automated Alerts**: Monitor for SLA breaches and system anomalies
- **Historical Analysis**: Maintain rolling 30-day performance history

## 🚀 Quick Start

1. **Review seeds/**: Live funnel specifications for constellation workflows
2. **Configure schemas/**: Funnel specification schema definitions  
3. **Generate signals/**: Create latest.json broadcast file
4. **Run validation**: `scripts/validate.sh`

## 📡 Broadcasting

This module produces a `signals/latest.json` file conforming to the constellation's broadcast schema. The Signal (📡) aggregates these across all stars.

## 🔗 Constellation Links

- **Hub**: [FourTwenty Analytics](https://github.com/zbreeden/FourTwentyAnalytics)
- **Archive**: Glossary, tags, and canonical definitions
- **Signal**: Cross-constellation broadcasting and telemetry

---

*This star is part of the FourTwenty Analytics constellation - a modular analytics sandbox where each repository is a specialized "model" within an orbital system.*
