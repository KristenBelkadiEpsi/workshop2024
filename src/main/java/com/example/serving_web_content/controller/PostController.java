package com.example.serving_web_content.controller;

import com.example.serving_web_content.entity.Post;
import com.example.serving_web_content.service.PostService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/post")
public class PostController {
    @Autowired
    private  PostService postService;

    @GetMapping
    public List<Post> getPostTexts() {
        return postService.getAllPostTexts();
    }

    @PostMapping
    public Post createPostText(@RequestBody Post post){
        return postService.savePostText(post);
    }
}
