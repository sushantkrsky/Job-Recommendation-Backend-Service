def recommend_jobs(user_profile, job_postings):
    recommended_jobs = []

    for job in job_postings:
        print(f"Checking job: {job.job_title} at {job.company}")  # Debug line

        # Check if the job title matches any desired roles
        role_match = job.job_title in user_profile.get('desired_roles', [])
        print(f"Role Match: {role_match}")

        # Check if the job type matches
        job_type_match = (user_profile.get('job_type') == job.job_type)
        print(f"Job Type Match: {job_type_match}")

        # Check experience level
        experience_match = (user_profile.get('experience_level') == job.experience_level)
        print(f"Experience Match: {experience_match}")

        # Check if the job location is in the user's preferred locations
        location_match = job.location in user_profile.get('locations', [])
        print(f"Location Match: {location_match}")

        # Check if any skill matches
        skill_match = any(skill in job.required_skills for skill in user_profile.get('skills', []))
        print(f"Skill Match: {skill_match}")

        # Add job to recommendations if all matches are found
        if role_match and job_type_match and experience_match and location_match and skill_match:
            recommended_jobs.append(job)

    return recommended_jobs
