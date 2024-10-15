package com.example.serving_web_content.repository;


import com.example.serving_web_content.entity.Post;
import org.springframework.data.jpa.repository.JpaRepository;

public interface PostRepository extends JpaRepository<Post, Long>{
}
