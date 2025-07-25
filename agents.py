from crewai import Agent
from tools import yt_tool



blog_researcher=Agent(
    role='Blog researcher from Youtube Videos',
    goal='get the relevant video content for the topic {topic} from YT channel',
    verbose=True,
    memory=True,
    backstory=(
        "Expert in understanding videos in AI Data Science , MAchine Learning And GEN AI and providing suggestion"
    ),
    tools=[yt_tool],
    allow_delegation=True
)


blog_writer=Agent(
    role='Blog Writer',
    goal='Narrate compelling tech stories about the video {topic} from YT video',
    verbose=True,
    memory=True,
    backstory=(
        "With a flair for simplifying complex topics, you craft"
        "engaging narratives that captivate and educate, bringing new"
        "discoveries to light in an accessible manner."
    ),
    tools=[yt_tool],
    llm=llm,
    allow_delegation=False
)