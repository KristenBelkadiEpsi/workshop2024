package com.example.serving_web_content.service;

import com.example.serving_web_content.entity.Post;
import org.springframework.stereotype.Service;
import com.example.serving_web_content.repository.PostRepository;
import org.springframework.beans.factory.annotation.Autowired;
import  java.util.List;
@Service
public class PostService {
    @Autowired
    private PostRepository postRepository;

    public  List<Post> getAllPostTexts(){
        return postRepository.findAll();
    }

    public Post savePostText(Post post){
        return postRepository.save(post);
    }
}
